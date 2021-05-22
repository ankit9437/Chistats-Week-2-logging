"""46. Update the value of the counter
		_count = Counter()
		_count.update('Welcome to python world!')
		print(_count)"""

from collections import Counter
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

_count = Counter()
_count.update('Welcome to python world!')
logging.warning(_count)

"""Output
21-May-21 19:03:23 - Counter({'o': 4, ' ': 3, 'e': 2, 'l': 2, 't': 2, 'W': 1, 'c': 1, 'm': 1, 'p': 1, 'y': 1, 'h': 1, 'n': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
"""