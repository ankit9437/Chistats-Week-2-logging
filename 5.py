#5. WAF which takes number as parameter and prints the square of it

import logging
def sqre(a):
    logging.debug(a*a)

a=int(input())
logging.basicConfig(filename= '5test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
sqre(a)
"""Output
20-May-21 15:21:54 - Admin logged in
20-May-21 15:21:54 - 16"""