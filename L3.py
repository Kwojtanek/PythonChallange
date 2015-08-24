__author__ = 'Jakub Wojtanek. Kwojtanek@gmail.com'
import re
def L3():
    xt = open('l3.txt', 'r')
    xt = xt.read()
    print ''.join(re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", xt))

L3()