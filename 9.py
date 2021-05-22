#10. WAF to get variable length argument and caculate the sum of square of those numbers

import logging
def eq(l):
    l1=[]
    for i in range(len(l)):
        x=l[i]*l[i]
        l1.append(x)
    return l1

l=[]
l=[int(x) for x in input().split()]
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug(eq(l))

"""Output
2 3 4 5
20-May-21 15:29:35 - [4, 9, 16, 25]"""