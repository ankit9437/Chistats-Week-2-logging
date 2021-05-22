#21. WAP to filter even numbers from list by using filter() function

import logging
lis1 = [1, 2, 3, 4, 5]

is_even = lambda x: x % 2 == 0
lis2 = list(filter(is_even, lis1))
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
logging.debug(lis2)

"""Output
20-May-21 15:39:16 - Admin logged in
20-May-21 15:39:16 - [2, 4]"""