s = [s for s in input()]
 
def check(s):
  if s[0] != "A":
      return False
  
  if s[2:-1].count("C") != 1:
      return False
  
  if sum(map(str.isupper, s)) != 2:
      return False
  
  return True
 
print("AC" if check(s) else "WA")
