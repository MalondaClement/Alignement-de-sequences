import cout
import dist
import numpy as np

def coupure (x, y, T) :
	n = len(x)+1
	m = len(y)+1
	p = (n-1)//2
	I = np.zeros((n, m))
	i = 1
	j = 1

	for i in range (1,n) :
		for j in range (1, m) :
			
			if (i<p) :
				I[i][j] = 0

			elif (i==p) :
				I[i][j] = j
			
			else :
				s = min (T[i-1][j], T[i][j-1], T[i-1][j-1])
				
				if (s == T[i-1][j]) :
					I[i][j] = I[i-1][j]
					
				elif (s == T[i][j-1]) :
					I[i][j] = I[i][j-1]

				elif (s == T[i-1][j-1]) :
					I[i][j] = I[i-1][j-1]
	return (I[n-1][m-1])

if __name__=="__main__" :
	print (coupure ("ATTGTA", "ATCTTA", dist.DIST_1 ("ATTGTA", "ATCTTA")[1]))
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
