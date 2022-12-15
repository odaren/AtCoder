n = int(input())
nums = list(map(int, input().split()))

if 0 in nums:
  ans = 0
else:
  ans = 1

for i in nums:
  ans = ans * i
  if ans > 10**18:
    break

if ans > 10**18:
  print(-1)
else:
  print(ans)
