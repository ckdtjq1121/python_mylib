import multiprocessing
import time

def func(idx):
  print('sub func {} start'.format(idx))
  time.sleep(5)
  print('sub func {} end'.format(idx))

def non_multi():
  print('main func start')
  for i in range(4):
    func(i)
  print('main func end')

def multi():
  print('main func start')
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i])
    p.start()
  print('main func end') # sub func보다 먼저 실행된다
  
def multi_join():
  print('main func start')
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i])
    p.start()
    p.join() # p가 끝나기를 기다린다
  print('main func end')

def multi_join_sep():
  print('main func start')
  jobs = []
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i])
    p.start()
    jobs.append(p)
  for p in jobs: 
    p.join() 
  print('main func end') # 모든 join이 끝난뒤 이부분이 실행된다

def multi_join_sep_timeout():
  '''
  0초 : main start
  0초 : 모든 서브 프로세스를 실행시킨다
  0~1초 : 0번째 p를 1초 기다린다
  1~2초 : 1번째 p를 1초 기다린다
  ..
  3~4초 : 3번째 p를 1초 기다린다
  4초 : main end
  5초 : 모든 서브 프로세스가 끝이 난다
  '''
  print('main func start')
  jobs = []
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i]) # 5초가 걸린다
    p.start()
    jobs.append(p)
  s = time.time()
  for p in jobs: 
    p.join(1) 
  e = time.time()
  print('main func end')
  print(e-s)
  
def multi_daemon():
  print('main func start')
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i], daemon=True)
    p.start()
  print('main func end') # sub func보다 먼저 실행된다 
  # + main func이 끝난뒤 sub func을 실행하지만 daemon이 True이기 때문에 sub들도 종료가 된다(시작도 안된다?)
 
def multi_daemon_join():
  print('main func start')
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i], daemon=True)
    p.start()
    p.join()
  print('main func end')
  
def multi_daemon_join_sep():
  print('main func start')
  jobs = []
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i], daemon=True)
    p.start()
    jobs.append(p)
  s = time.time()
  for p in jobs: 
    p.join() # p 가 끝날때 까지 무한정 기다린다
  e = time.time()
  
  print('main func end')
  print(e-s)
  
def multi_daemon_join_sep_timeout():
  print('main func start')
  jobs = []
  for i in range(4):
    p = multiprocessing.Process(target=func, args=[i], daemon=True)
    p.start()
    jobs.append(p)
  
  s = time.time()
  for p in jobs: 
    p.join(1) 
  e = time.time()
  
  print('main func end')
  print(e-s)
  
if __name__ == '__main__':
  # non_multi()
  # multi()
  # multi_join()
  # multi_join_sep()
  # multi_join_sep_timeout()
  # multi_daemon()
  # multi_daemon_join()
  # multi_daemon_join_sep()
  multi_daemon_join_sep_timeout()
  