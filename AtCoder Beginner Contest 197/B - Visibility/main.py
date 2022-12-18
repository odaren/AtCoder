# 二次元盤面

i = list(map(int, input().split()))
s = [input() for i in range(i[0])]

# 変数の定義
H = i[0]
W = i[1]
X = i[2]
Y = i[3]

# 配列のインデックスに合わせる
X -= 1
Y -= 1

count = 1

# マスの上方向を攻める
for i in range(1, 101):
  if X - i < 0 or s[X - i][Y] == "#":
    break
  else:
    # print("上にありました")
    count += 1

# マスの下方向を攻める
for i in range(1, 101):
  if X + i == H or s[X + i][Y] == "#":
    break
  else:
    # print("下にありました")
    count += 1

# マスの左方向を攻める
for i in range(1, 101):
  if Y - i < 0 or s[X][Y - i] == "#":
    break
  else:
    # print("左にありました")
    count += 1

# マスの右方向を攻める
for i in range(1, 101):
  if Y + i == W or s[X][Y + i] == "#":
    break
  else:
    # print("右にありました")
    count += 1
    
print(count)
