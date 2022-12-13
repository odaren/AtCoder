import math
 
n = int(input())
 
count = 0
money = 100
 
while money < n:
  money = money + (money // 100)
  count = count + 1
 
print(count)
