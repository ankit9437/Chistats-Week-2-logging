#22. WAP to filter students whoes name starts with "a" by using filter() function

import logging
lis1 = ['ankt','ashu','sarthak','kunal']

is_a = lambda x: x[0] == 'a'
lis2 = list(filter(is_a, lis1))
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
logging.debug(lis2)

"""Output
20-May-21 16:42:38 - Admin logged in
20-May-21 16:42:38 - ['ankt', 'ashu']"""