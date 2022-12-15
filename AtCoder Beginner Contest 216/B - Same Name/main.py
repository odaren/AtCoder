n = int(input())
x = [input() for _ in range(n)]
 
ans = "No"
 
for i in x:
  if x.count(i) >= 2:
    ans = "Yes"
    break
    
print(ans)
