def LCS (a, b):
	L = [[0]*(len (b)+1) for i in range (len (a) + 1)]
	for i in range (1, len (a)+1):
		for j in range (1, len (b) + 1):
			if a[i-1] == b[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max (L[i-1][j], L[i][j-1])
	return L[len(a)][len(b)]

def main ():
	# navie solution:
	# iterate all words in the dictionairy to reply "did you mean"
	pass

if __name__ == "__main__":
	main ()