#51. WAP to get all elements with positive value and count>0 from counter

import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

l=[2,4,-5,8,-10,5,-8]
for i in range(len(l)):
    if(l[i]>0):
        logging.warning(l[i])

"""Output
21-May-21 19:08:02 - 2
21-May-21 19:08:02 - 4
21-May-21 19:08:02 - 8
21-May-21 19:08:02 - 5"""