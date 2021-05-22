"""54. Iterate on the below using enumerate() function
	my_list = ["eat","sleep","repeat"]
	my_str = "chistats"
	my_tuple = ("A", "B", "C", "D", "E")
	my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}
	Explain the output of the enumerator"""

import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

my_list = ["eat","sleep","repeat"]
my_str = "chistats"
my_tuple = ("A", "B", "C", "D", "E")
my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}

logging.warning(list(enumerate(my_list)))
logging.warning(list(enumerate(my_str)))
logging.warning(tuple(enumerate(my_tuple)))
logging.warning(dict(enumerate(my_dict)))

"""Output
21-May-21 19:10:29 - [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
21-May-21 19:10:29 - [(0, 'c'), (1, 'h'), (2, 'i'), (3, 's'), (4, 't'), (5, 'a'), (6, 't'), (7, 's')]
21-May-21 19:10:29 - ((0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'))
21-May-21 19:10:29 - {0: 'a', 1: 'b', 2: 'c', 3: 'd'}"""