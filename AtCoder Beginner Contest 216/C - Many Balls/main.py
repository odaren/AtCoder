n = int(input())
a = []
 
while n > 0:
  if n % 2 == 0:
    n = n // 2
    a.append('B')
  else:
    n = n - 1
    a.append('A')
 
a.reverse()
 
print(''.join(a))
