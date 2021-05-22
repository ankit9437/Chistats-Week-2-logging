"""45. What will be the output of below

	1. 	my_str = "Welcome to python world!"
		Counter(my_str)

	2. 	dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
		Counter(dict1)

	3.  tuple1 = ('x','y','z','x','x','x','y','z')
		Counter(tuple1)"""

from collections import Counter
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

my_str = "Welcome to python world!"
logging.warning(Counter(my_str))
dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
logging.warning(Counter(dict1))
tuple1 = ('x','y','z','x','x','x','y','z')
logging.warning(Counter(tuple1))

"""Output
21-May-21 19:01:42 - Counter({'o': 4, ' ': 3, 'e': 2, 'l': 2, 't': 2, 'W': 1, 'c': 1, 'm': 1, 'p': 1, 'y': 1, 'h': 1, 'n': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
21-May-21 19:01:42 - Counter({'x': 4, 'y': 2, 'z': 2})
21-May-21 19:01:42 - Counter({'x': 4, 'y': 2, 'z': 2})"""