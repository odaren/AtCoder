def check():
  n = int(input())
  ls = [list(map(int, input().split())) for _ in range(n)]

  pt, px, py = 0, 0, 0

  for i in ls:
    t, x, y = i[0], i[1], i[2]
    T, X, Y = t - pt, abs(x- px), abs(y - py)

    if T < X + Y:
      return False
    
    if T % 2 != (X + Y) % 2:
      return False
    
    pt, px, py = t, x, y
    
  return True

print("Yes" if check() else "No")
