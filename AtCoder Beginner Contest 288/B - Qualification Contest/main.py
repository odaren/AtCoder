i = list(map(int, input().split())) # リスト
N = i[0]
M = i[1]
s = [input() for i in range(N)]

target = s[0:M]
target.sort()
for i in range(len(target)):
  print(target[i])
