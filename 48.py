"""49. SUppoer we have two counter mentioned below
counter1 =  Counter({'x': 4, 'y': 2, 'z': -2})
counter2 = Counter({'x1': -12, 'y': 5, 'z':4 })
Perform below operations on the conters
	1. Addiotion
	2. Subtraction
	3. Intersection
	4. Union"""

from collections import Counter
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

c1 = Counter(a=2, b=0, c=-1)
c2 = Counter(a=1, b=-1, c=2)

c = c1 + c2
logging.warning(c)

c = c1 - c2
logging.warning(c)

c = c1 & c2
logging.warning(c)

c = c1 | c2
logging.warning(c)

"""Output
21-May-21 19:05:57 - Counter({'a': 3, 'c': 1})
21-May-21 19:05:57 - Counter({'a': 1, 'b': 1})
21-May-21 19:05:57 - Counter({'a': 1})
21-May-21 19:05:57 - Counter({'a': 2, 'c': 2})"""