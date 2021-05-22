"""27. Nested function: Create a function which takes the list of numbers as parameter, calculates the square of every number in the nexted function and returns the final list of squares.
"""
import logging
def fun(l):
    def ret(l1):
        return l1
    l1=[]
    for i in l:
        l1.append(i*i)
    print(ret(l1))


l=[2,3,4,5]
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
logging.debug(fun(l))

"""Output
20-May-21 16:47:59 - Admin logged in
20-May-21 16:47:59 - None
[4, 9, 16, 25]
"""