def check(N,n,s):
	cnt=0
	for i in range(N-n):
		if s[i] != s[i+n]:
			cnt+=1
		else:
			break
	return cnt

def main():
	N=int(input())
	S=input()
	for i in range(1, N):
		print(check(N,i,S))

if __name__=="__main__":
	main()
