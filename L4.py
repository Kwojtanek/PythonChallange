__author__ = 'Jakub Wojtanek. Kwojtanek@gmail.com'
import urllib2, re

def L4(noth = 21545, i=100):
    print i
    if noth:
        l = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(noth)
        s = urllib2.urlopen(l)
        s = s.read()
        print s
        if re.findall("\d+$", s):
            noth = re.findall("\d+$", s)[0]
            i +=1
            print noth
            L4(noth, i)
