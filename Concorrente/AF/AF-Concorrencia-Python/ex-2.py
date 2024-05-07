from time import sleep
from random import randint
from threading import Thread, Semaphore, Lock

def produtor(id: int):
  global buffer, sem_vazio, sem_cheio
  for i in range(10):
    item = 'item ' + str(i)
    sem_vazio.acquire()
    with lock:
      buffer.append(item)
      print('Thread %i -> Produzido %s (ha %i itens no buffer)' % (id,item,len(buffer)))
      sem_cheio.release()  

def consumidor(id: int):
  global buffer, sem_vazio, sem_cheio
  for i in range(10):
    sem_cheio.acquire()
    with lock:
      item = buffer.pop(0)
      print('Thread %i -> Consumido %s (ha %i itens no buffer)' % (id, item,len(buffer)))
      sem_vazio.release()

buffer = []
tam_buffer = 3
lock = Lock()

sem_vazio = Semaphore(tam_buffer)
sem_cheio = Semaphore(0)
num_threads = 1

consumidores = [Thread(target=consumidor, args=[id]) for id in range(num_threads)]
produtores = [Thread(target=produtor, args=[id]) for id in range(num_threads, num_threads*2)]
[(t1.start(), t2.start()) for t1, t2 in zip(produtores, consumidores)]
[(t1.join(), t2.join()) for t1, t2 in zip(produtores, consumidores)]
