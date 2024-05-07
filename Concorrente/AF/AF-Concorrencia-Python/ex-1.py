from time import sleep
from random import randint
from threading import Thread, Lock, Condition

def produtor(id: int):
  global buffer
  for i in range(10):
    sleep(randint(0,2))           # fica um tempo produzindo...
    item = 'item ' + str(i)
    with lugar_no_buffer:
      while len(buffer) >= tam_buffer:
        print('Thread %i -> >>> Buffer cheio. Produtor ira aguardar.' % (id))
        lugar_no_buffer.wait()    # aguarda que haja lugar no buffer
      buffer.append(item)
      print('Thread %i -> Produzido %s (ha %i itens no buffer)' % (id, item,len(buffer)))
      item_no_buffer.notify()

def consumidor(id: int):
  global buffer
  for i in range(10):
    with item_no_buffer:
      while not buffer:
        print('Thread %i -> >>> Buffer vazio. Consumidor ira aguardar.' % (id))
        item_no_buffer.wait()   # aguarda que haja um item para consumir 
      item = buffer.pop(0)
      print('Thread %i -> Consumido %s (ha %i itens no buffer)' % (id, item,len(buffer)))
      lugar_no_buffer.notify()
    sleep(randint(0,2))         # fica um tempo consumindo...

buffer = []
tam_buffer = 5
num_threads = 2
lock = Lock()
lugar_no_buffer = Condition(lock)
item_no_buffer = Condition(lock)


produtores = [Thread(target=produtor, args=[id]) for id in range(num_threads)]
consumidores = [Thread(target=consumidor, args=[id]) for id in range(num_threads, num_threads*2)]
[(t1.start(), t2.start()) for t1, t2 in zip(produtores, consumidores)]
[(t1.join(), t2.join()) for t1, t2 in zip(produtores, consumidores)]

