#40. WAP to print the number from list with pause of 5 seconds

import time
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

l=[12,23,45,67,78]
for i in l:
    logging.warning(i)
    time.sleep(5)

"""Output
21-May-21 15:00:10 - 12
21-May-21 15:00:15 - 23
21-May-21 15:00:20 - 45
21-May-21 15:00:25 - 67
21-May-21 15:00:30 - 78"""