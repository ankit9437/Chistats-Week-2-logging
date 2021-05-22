#34. WAP to create a list of even number between the given numbers using range()


import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

a=12
b=17
for i in range(a,b+1):
    if(i%2==0):
        logging.warning(i)

"""Output
21-May-21 14:54:10 - 12
21-May-21 14:54:10 - 14
21-May-21 14:54:10 - 16"""