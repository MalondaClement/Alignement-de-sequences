import dist
import cout

def SOL_1 (x, y, T) :
	u = ""
	v = ""
	n = len(x) 
	m = len(y) 
	i = n
	j = m
	
	while (i >= 1) or (j >= 1) :
		
		if (i == 1) :
			u = x[i-1] + u
			while (j>=1) :
				u = "-" + u
				v = y[j-1] + v
				j= j -1
			v = y[j-1] + v
			return (u, v)

		elif j == 1 :
			v = y[i-1] + v
			while (i>=1) :
				v = "-" + v
				u = x[i-1] + u
				i = i -1
			u = u[i-1] + u
			return (u, v)
		
		elif (T[i][j]) == (T[i-1][j] + 2) :
			u = x[i-1] + u 
			v = "-" + v
			i = i - 1
			
		elif (T[i][j]) == (T[i][j-1] + 2) :
			u = "-" + u 	
			v = y[j-1] + v 
			j = j - 1  
			
		elif T[i][j] == (T[i-1][j-1] + cout.c_sub (x[i-1], y[j-1])) :
			u = x[i-1] + u
			v = y[j-1] + v
			i = i - 1
			j = j - 1
	return (u, v)
	
	


if __name__=="__main__" :
	#print (len("ATTGTA"), len ("ATCTTA"))
	print (SOL_1 ("ATTGTA", "ATCTTA", dist.DIST_1 ("ATTGTA", "ATCTTA")[1] ))
	print (SOL_1 ("ATCG", "GCTGA", dist.DIST_1 ("ATCG", "GCTGA")[1] ))
