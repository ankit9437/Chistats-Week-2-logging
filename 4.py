#4. WAF which takes name as parameter and prints it

import logging
def name(nam):
    logging.debug(nam)

s=input()
logging.basicConfig(filename= '4test.log',level=logging.DEBUG)
logging.info('Admin logged in')
name(s)


"""Output
INFO:root:Admin logged in
ERROR:root:Ankit raised an output
INFO:root:Admin logged in
ERROR:root:Ankit raised an output
INFO:root:Admin logged in
DEBUG:root:Ankit"""