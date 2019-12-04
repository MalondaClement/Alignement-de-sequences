import cout
import numpy as np

def DIST_1 (x, y) :
	n = len(x)+1
	m = len(y)+1
	T = np.zeros((n, m))

	for i in range (n):
		for j in range (m) :
			#if (i!=0) and (j!=) :
			if (i==0) :
				T[i][j] = j*2

			elif (j==0):
				T[i][j] = i*2
			else :
				T[i][j] = min (T[i-1][j]+2, T[i][j-1] + 2, T[i-1][j-1] + cout.c_sub (x[i-1], y[j-1]))

	return (T[n-1][m-1], T)

if __name__=="__main__" :
	print (DIST_1 ("ATTGTA", "ATCTTA"))
	print (DIST_1 ("", "ATTGC"))
	print (DIST_1 ("AGCTA", ""))
