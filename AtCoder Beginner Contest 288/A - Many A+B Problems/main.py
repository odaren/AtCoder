n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  print(ls[i][0] + ls[i][1])
