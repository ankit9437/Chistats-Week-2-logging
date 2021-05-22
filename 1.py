#3. WAF to print "Hello World"

import logging
def hell():
    logging.debug("Hello World")


logging.basicConfig(filename= 'test.log',level=logging.DEBUG)
logging.info('Admin logged in')
name = 'Ankit'

logging.error('%s raised an output', name)
hell()

"""Output
DEBUG:root:Hello World
INFO:root:Admin logged in
ERROR:root:Ankit raised an output
DEBUG:root:Hello World"""