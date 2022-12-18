L = list(map(int, input().split()))
N = L[0]
Y = L[1]

A, B, C = -1, -1, -1

for a in range(N + 1):
  for b in range(N + 1):
    c = N - a - b
    
    if c < 0:
      continue
    
    if 10000 * a + 5000 * b + 1000 * c == Y:
      A, B, C, = a, b, c

print(A, B, C)
