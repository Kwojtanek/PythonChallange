import pickle
__author__ = 'Jakub Wojtanek. Kwojtanek@gmail.com'
def L5():
    k = open('l5.txt')
    k = pickle.load(k)
    for x in range(0,len(k)):
        line = ''
        for y in range(0,len((k[x]))):
            line = line + str(k[x][y][0])*int(str(k[x][y][1]))
        print line
L5()