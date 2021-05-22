"""23. WAP to get list of integers as input and generate another list containing the square of all integers from list one. Write using lambda function and also without using lambda function"""

import logging
nums = [1, 2, 3, 4, 5]
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
logging.debug("Original list of integers:")
logging.debug(nums)
logging.debug("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
logging.debug(square_nums

"""Output
20-May-21 16:44:10 - Admin logged in
20-May-21 16:44:10 - Original list of integers:
20-May-21 16:44:10 - [1, 2, 3, 4, 5]
20-May-21 16:44:10 - 
Square every number of the said list:
20-May-21 16:44:10 - [1, 4, 9, 16, 25]"""