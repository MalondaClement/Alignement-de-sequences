import dist
import cout
import sys
import lectureFichier

def DIST_2 (x, y):
    n = len(x)
    m = len(y)
    T[2][m]
    for i in range (n) :
        for j in range (m) :
                if i== 0:
                        T[i][j] = 2*j
                if j==0 :
                        T[i][j] = 2*i
                T[i-1][j] = T[i][j]
                T[i][j] = min (T[i-1][j] + 2, T[i][j-1]+2, T[i-1][j-1] + cout.c_sub(x(i-1), y(j-1))

if __name__=="__main__":
    if(len(sys.argv) != 1):
        x,y = lectureFichier.LIRE_FICHER_ADN(sys.argv[1])
        x,y = sol_1.SOL_1(x, y,     DIST_2(x,y)[1])
        print(x)
        print(y)
    else:
        print("Il faut passer une instance de genome en argument")
