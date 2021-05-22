"""12. Function
	def fun(arg1, arg2, arg3=4, arg4=8):
		print(arg1, arg2,arg3,arg4)

What will be the output of the below function calls
	1. fun(3,2)
	2. fun(10, 20, 30, 40)
	3. fun(25, 50, arg4=10)
	4. fun(arg4=4, arg1=3, arg2=4)
	5. fun()
	6. fun(arg3=10, arg4=20, 30, 40)
	7. fun(4, 5, arg2=6)
	8. fun(4, ,5 arg3=5, arg5=6)"""

import logging
def fun(arg1, arg2, arg3=4, arg4=8):
    print(arg1, arg2, arg3, arg4)

logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug(fun(3,2))
logging.debug(fun(10, 20, 30, 40))
logging.debug(fun(25, 50, arg4=10))
logging.debug(fun(arg4=4, arg1=3, arg2=4))

"""Output
3 2 4 8
10 20 30 40
25 50 4 10
3 4 4 4

20-May-21 15:31:46 - None
20-May-21 15:31:46 - None
20-May-21 15:31:46 - None
20-May-21 15:31:46 - None"""