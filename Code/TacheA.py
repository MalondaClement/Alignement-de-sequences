import math
import sys
import lectureFichier
import cout

##fonction distance naive
def DIST_NAIF(x,y):
    return DIST_NAIF_REC(x, y, 0, 0, 0, math.inf)

##fonction distance naive recursive
def DIST_NAIF_REC(x, y, i, j, c, dist):
    if len(x)-1 == i and len(y)-1 == j: ## ici on est oblige de faire -1 sur la taiile de la string car sinon on peut faire un IndexOutOfRange
        if c < dist:
            dist = c
    else:
        if (i < len(x)-1 and j < len(y)-1): ## ici on est oblige de faire -1 sur la taile de la string car sinon on peut faire un IndexOutOfRange a la ligne suivante
            dist = DIST_NAIF_REC(x, y, i+1, j+1, c + cout.c_sub(x[i+1], y[j+1]), dist)
        if i < len(x)-1: ## test avec le -1
            dist = DIST_NAIF_REC(x, y, i+1, j, c + cout.c_del(), dist)
        if j < len(y)-1: ## test avec le -1
            dist = DIST_NAIF_REC(x, y, i, j+1, c + cout.c_ins(), dist)
    return dist

if __name__=="__main__":
    if(len(sys.argv) != 1):
        x,y = lectureFichier.LIRE_FICHER_ADN(sys.argv[1])
        print(DIST_NAIF(x, y))
    else:
        print("Il faut passer une instance de genome en argument")
