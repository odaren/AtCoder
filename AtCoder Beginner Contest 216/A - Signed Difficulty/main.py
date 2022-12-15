n = input().split('.')
 
if int(n[1]) <= 2:
  print(n[0] + '-')
elif int(n[1]) <= 6:
  print(n[0])
else:
  print(n[0] + '+')
