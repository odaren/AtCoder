i = list(map(int, input().split()))
N, Q = i[0], i[1]
s = input()

cs = [0] * (N + 1)
for i in range(1, N):
  cs[i + 1] = cs[i] + (s[i - 1:i + 1] == "AC")

for q in range(Q):
  l, r = map(int, input().split())  
  print(cs[r] - cs[l])
