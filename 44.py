"""44. Using Counter: WAP to get the count of number of occurences of alphabet present in the list1 = ['x','y','z','x','x','x','y', 'z'] hint : from collections import Counter
"""
from collections import Counter
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

# With sequence of items
logging.warning(Counter(['x','y','z','x','x','x','y', 'z']))

"""Output
21-May-21 15:07:23 - Counter({'x': 4, 'y': 2, 'z': 2})"""