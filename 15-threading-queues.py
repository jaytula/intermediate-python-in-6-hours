from threading import Thread, Lock
from queue import Queue
import time

if __name__ == "__main__":
  q = Queue()

  q.put(1)
  q.put(2)
  q.put(3)

  # 3 2 1
  first = q.get()
  print(first) # 1

  isEmpty = q.empty()

  q.task_done()

  q.join() # blocks until all elements in queue are processed
  print('end main')
