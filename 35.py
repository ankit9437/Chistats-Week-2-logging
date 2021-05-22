#35. What will be the output of range(2, -14, -2)


import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

for i in range(2,-14,-2):
    logging.warning(i)

"""Output
21-May-21 14:55:08 - 2
21-May-21 14:55:08 - 0
21-May-21 14:55:08 - -2
21-May-21 14:55:08 - -4
21-May-21 14:55:08 - -6
21-May-21 14:55:08 - -8
21-May-21 14:55:08 - -10
21-May-21 14:55:08 - -12"""