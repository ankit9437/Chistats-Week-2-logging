#19. Write a lambda function to get sum of two given numbers

import logging
a=[12,34]
add = lambda x: x[0]+x[1]>0
lis2 = list(filter(add, a))
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug(lis2)