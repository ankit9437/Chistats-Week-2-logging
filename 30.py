"""30. What will be the output of below
	1. abs(-7.25)
	2. abs(3+5j)
	3. abs(3 - 4j)
	4. round(5.76543, 2)
	5. round(5.76543)
	6. round(-1.2)
	7. arr = [-0.341111, 1.455098989, 4.232323, -0.3432326, 7.626632, 5.122323]"""

import logging

arr = [-0.341111, 1.455098989, 4.232323, -0.3432326, 7.626632, 5.122323]
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
logging.debug(abs(-7.25))
logging.debug(abs(3+5j))
logging.debug(abs(3 - 4j))
logging.debug(round(5.76543, 2))
logging.debug(round(5.76543))
logging.debug(round(5.76543))
logging.debug(round(-1.2))

"""Output
20-May-21 16:50:13 - Admin logged in
20-May-21 16:50:13 - 7.25
20-May-21 16:50:52 - Admin logged in
20-May-21 16:50:52 - 7.25
20-May-21 16:50:52 - 5.830951894845301
20-May-21 16:50:52 - 5.0
20-May-21 16:50:52 - 5.77
20-May-21 16:50:52 - 6
20-May-21 16:50:52 - 6
20-May-21 16:50:52 - -1"""