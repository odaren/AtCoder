N = int(input())
L = list(map(int, input().split()))
L = sorted(L, reverse=True)

a, b = 0, 0

for i in range(N):
  if i % 2 == 0:
    a = a + L[i]
  else:
    b = b + L[i]
    
print(a - b)
