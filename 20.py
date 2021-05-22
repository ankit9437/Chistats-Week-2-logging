#20. Write a lambda function to get max of given values
import sys
import logging
myList = [1,2,3,10,4,5,6,7,8,9]

def maxVal(list_a, compare_function):
    max = -sys.maxsize - 1
    for i in list_a:
        if compare_function(i, max):
            max = i
    return max

my_compare_function = lambda x,y: max(x, y)
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug(maxVal(myList, my_compare_function))

"""Output
20-May-21 15:37:23 - 9"""