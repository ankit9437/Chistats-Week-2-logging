#33. WAP to create a sequence of numbers from 3 to 19, but increment by 2 instead of 1

import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
for i in range(3,20,2):
    logging.warning(i)

"""Output
21-May-21 14:53:12 - 3
21-May-21 14:53:12 - 5
21-May-21 14:53:12 - 7
21-May-21 14:53:12 - 9
21-May-21 14:53:12 - 11
21-May-21 14:53:12 - 13
21-May-21 14:53:12 - 15
21-May-21 14:53:12 - 17
21-May-21 14:53:12 - 19"""