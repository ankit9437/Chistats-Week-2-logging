#52. WAP to get count of specific element from counter

import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

from collections import Counter
a_list = ["a", "b", "a",'f','a','b']
occurrences = Counter(a_list)
logging.warning(occurrences)
logging.warning(occurrences["a"])

"""Output
21-May-21 19:09:06 - Counter({'a': 3, 'b': 2, 'f': 1})
21-May-21 19:09:06 - 3"""