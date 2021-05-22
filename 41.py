#41. WAP to create the queue using collections.dequeue and perform all the queue operations like append, popleft

from collections import deque
import time
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

# Declaring deque
queue = deque([1,2,3,4])
logging.warning(queue)
queue.append(8)
logging.warning("Appended queuq",queue)
logging.warning("\nElements dequeued from the queue")
logging.warning(queue.popleft())

import collections
de = collections.deque([1, 2, 3])
logging.warning(de)
de.append(4)
logging.warning("The deque after appending at right is : ")
logging.warning(de)
de.popleft()
logging.warning("The deque after deleting from left is : ")
logging.warning(de)

"""Output
21-May-21 15:02:31 - deque([1, 2, 3, 4])
21-May-21 15:02:31 - 
Elements dequeued from the queue
21-May-21 15:02:31 - 1
21-May-21 15:02:31 - deque([1, 2, 3])
21-May-21 15:02:31 - The deque after appending at right is : 
21-May-21 15:02:31 - deque([1, 2, 3, 4])
21-May-21 15:02:31 - The deque after deleting from left is : 
21-May-21 15:02:31 - deque([2, 3, 4])"""