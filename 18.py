#18. Write a lambda function to get square of given numbers

import logging
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug("Original list of integers:")
logging.debug(nums)
logging.debug("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
logging.debug(square_nums)

"""Output
20-May-21 15:34:50 - Original list of integers:
20-May-21 15:34:50 - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
20-May-21 15:34:50 - 
Square every number of the said list:
20-May-21 15:34:50 - [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"""