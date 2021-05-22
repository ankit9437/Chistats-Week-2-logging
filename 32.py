#32. WAP to create a sequence of numbers from 3 to 5 using range()

import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
for i in range(3,6):
    logging.warning(i)

"""Output
21-May-21 14:51:46 - 3
21-May-21 14:51:46 - 4
21-May-21 14:51:46 - 5"""