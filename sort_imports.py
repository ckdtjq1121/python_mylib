imports = []
froms = []
def line_input_and_calc():
    line = input()
    if line == '':
        return 1
    
    global imports, froms
    if line.split(' ', 1)[0] == 'import':     
        l = line.split(' ', 1)
            
        args = l[1].split(',')
        args = [i.strip() for i in args]
        args.sort()
        
        line = 'import'
        for i in range(len(args)):
            line += ' '+args[i]
            if i != len(args)-1:
                line += ',' 
        imports.append(line)
    elif line.split(' ', 1)[0] == 'from':
        l = line.split(' ', 1)[1]
        ll = l.split('import')
        args = ll[1].split(',')
        args = [i.strip() for i in args]
        args.sort()
            
        line = 'from '+ ll[0] + 'import'
        for i in range(len(args)):
            line += ' '+args[i]
            if i != len(args)-1:
                line+=','
        froms.append(line) 
        
        

def abcImport():
    global imports, froms
    while(1):
        ret = line_input_and_calc()
        if ret == 1:
            break
        
    imports.sort()
    froms.sort()
    for i in imports:
        print(i)
    for i in froms:
        print(i)        
    
abcImport()