N = int(input())
L = list(map(int, input().split()))

count = 0

while True:
  can_do = True
  
  for i in range(N):
    if L[i] % 2 == 1:
      can_do = False
  
  if not can_do:
    break
    
  for i in range(N):
    L[i] = L[i] // 2
  
  count += 1

print(count)
