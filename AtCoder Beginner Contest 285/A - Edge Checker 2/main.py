i = list(map(int, input().split()))
a, b = i[0], i[1]

if b == a * 2 or b == a * 2 + 1:
  print("Yes")
else:
  print("No")
