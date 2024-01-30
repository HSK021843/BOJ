def check_validity(k, col):
	for i in range(1, k):
		if x[i] == col or abs(i - k) == abs(x[i] - col):
			return False
	return True
	
def n_queens(k):
	global ans
	if k > n:
		ans += 1
		return
		
	for col in range(1, n+1):
		if check_validity(k, col):
			x[k] = col
			n_queens(k+1)


n = int(input())
x = [0]*(n+1)
ans = 0
n_queens(1)

print(ans)
