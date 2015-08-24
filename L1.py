__author__ = 'Jakub Wojtanek. Kwojtanek@gmail.com'
from string import maketrans

def L1():
    st = "http://www.pythonchallenge.com/pc/def/map.html"
    al = 'abcdefghijklmnopqrstuvwxyz'
    aln ='cdefghijklmnopqrstuvwxyzab'
    trantab = maketrans(al, aln)
    return st.translate(trantab)
L1()