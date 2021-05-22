#50. WAP to get the most common elements from the counter

from collections import Counter
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


List = [2, 1, 2, 2, 1, 3]
logging.warning(most_frequent(List))

"""Output
21-May-21 19:07:00 - 2"""