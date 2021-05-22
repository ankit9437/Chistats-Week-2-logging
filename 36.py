#38. WAP to get all square numbers from 1 to 100 using yield. Ex. 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

def nextSquare():
    i = 1;
    while True:
        yield i * i
        i += 1
for num in nextSquare():
    if num > 100:
        break
    logging.warning(num)

"""Output
21-May-21 14:56:32 - 1
21-May-21 14:56:32 - 4
21-May-21 14:56:32 - 9
21-May-21 14:56:32 - 16
21-May-21 14:56:32 - 25
21-May-21 14:56:32 - 36
21-May-21 14:56:32 - 49
21-May-21 14:56:32 - 64
21-May-21 14:56:32 - 81
21-May-21 14:56:32 - 100"""