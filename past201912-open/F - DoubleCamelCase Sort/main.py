s = input()

words = []
i = 0
while i < len(s):
  # 大文字のs[i]を見つける
  j = i + 1
  while j < len(s) and s[j].islower():
    j = j + 1
  
  words.append(s[i:j + 1])
  i = j + 1
  
words.sort(key=str.lower)
print("".join(words))
