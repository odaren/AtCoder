input = list(map(int, input().split()))
H = input[0]
A = input[1]

if H % A == 0:
  print(H // A)
else:
  print(H // A + 1)
  
