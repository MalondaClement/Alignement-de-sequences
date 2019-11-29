import dist
import cout
import sys
import lectureFichier

def SOL_1 (x, y, T) :
	u = ""
	v = ""
	n = len(x)
	m = len(y)
	i = n
	j = m

	if (n==0) :
		u = m*"-"
		v = y
		return (u,v)
	elif (m==0) :
		u = x
		v = n*"-"
		return (u,v)

	while (i >= 1) or (j >= 1) :

		if (i==1) :
			u = x[i-1] + u
			if (j==1) :
				v = y[j-1] + v
				return (u,v)
			else :
				while (j>=1) :
					u = "-" + u
					v = y[j-1] + v
					j= j -1
				v = y[j] + v
				return (u, v)

		elif (j == 1) and (i>0) :
			v = y[i-1] + v

			while (i>=1) :
				v = "-" + v
				u = x[i-1] + u
				i = i -1
			u = x[i] + u
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
	if(len(sys.argv) != 1):
		x,y = lectureFichier.LIRE_FICHER_ADN(sys.argv[1])
		x,y = SOL_1(x, y, dist.DIST_1(x,y)[1])
		print(x)
		print(y)
		#print(x[:20])
		#print(y[:20])
	else:
		print("Il faut passer une instance de genome en argument")
		print (SOL_1 ("ATTGTA", "ATCTTA", dist.DIST_1 ("ATTGTA", "ATCTTA")[1] ))
		print (SOL_1 ("ATCG", "GCTGA", dist.DIST_1 ("ATCG", "GCTGA")[1] ))
