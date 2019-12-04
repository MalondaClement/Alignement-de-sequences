import coupure
import cout
import sys
import lectureFichier

def SOL_2(x, y):
    if len(y) == 0:
        return (x,mot_gaps(len(x)))
    if len(x) == 1 and len(y) == 1:
        if x == y :
            return (x,y)
        else:
            return (x+"-", "-"+y)
    else:
        res1 = SOL_2(x[:len(x)/2],y[:coupure.coupure(x,y)])
        res2 = SOL_2(x[len(x)/2:],y[coupure.coupure(x,y):])
        return (res1[0]+res2[0], res1[1]+res2[1])

if __name__=="__main__" :
    if(len(sys.argv) != 1):
        x,y = lectureFichier.LIRE_FICHER_ADN(sys.argv[1])
        x,y = SOL_2(x, y)
        print(x)
        print(y)
    else :
        print("Il faut passer une instance de genome en argument")
