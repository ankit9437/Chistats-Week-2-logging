"""42. WAP to create queue using using queue.Queue andperform below operations on it
	1. maxsize
	2. empty()
	3. full()
	4. get()
	5. get_nowait()
	6. put(item)
	7. put_nowait(item)
	8. qsize()"""

from queue import Queue

import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

q = Queue(maxsize=3)
logging.warning(q.qsize())
q.put('a')
q.put('b')
q.put('c')
logging.warning("\nFull: ", q.full())
logging.warning("\nElements dequeued from the queue")
logging.warning(q.get())
logging.warning(q.get())
logging.warning(q.get())
logging.warning("\nEmpty: ", q.empty())

q.put(1)
logging.warning("\nEmpty: ", q.empty())
logging.warning("Full: ", q.full())

"""Output
21-May-21 15:05:30 - 0
21-May-21 15:05:30 - 
Elements dequeued from the queue
21-May-21 15:05:30 - a
21-May-21 15:05:30 - b
21-May-21 15:05:30 - c"""