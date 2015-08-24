__author__ = 'Jakub Wojtanek. Kwojtanek@gmail.com'
import re
def L2():
    xt = open('l2.txt', 'r')
    xt = xt.read()
    print ''.join(re.findall("[A-Za-z]", xt))
l2()