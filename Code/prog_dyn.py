import dist
import sol_1


def PROG_DYN (x, y) :
	return (dist.DIST_1(x, y), sol_1.SOL_1(x, y, dist.DIST_1 (x, y)[1]))

if __name__=="__main__" :
	print ('1.',PROG_DYN ("ATTGTA", "ATCTTA"))
	print ('2', PROG_DYN ("TGTA", ""))
	print ('3.',PROG_DYN ("", "AATG"))
	print ('4.',PROG_DYN ("AAAAAAAGC", "AAAATAAGC"))	
