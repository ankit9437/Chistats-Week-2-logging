#24. WAP to calculate the sum of al numbers present in the list using reduce()

import functools
import logging
lis = [1, 3, 5, 6, 2, ]
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
logging.debug("The sum of the list elements is : ")
logging.debug(functools.reduce(lambda a, b: a + b, lis))

"""Output
20-May-21 16:45:43 - Admin logged in
20-May-21 16:46:02 - Admin logged in
20-May-21 16:46:02 - The sum of the list elements is : 
20-May-21 16:46:02 - 17"""