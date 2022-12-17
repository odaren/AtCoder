DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]
 
H, W = map(int, input().split())
S = [input() for i in range(H)]
 
result = [[0 if v == "." else "#" for v in row] for row in S]
 
for i in range(H):
  for j in range(W):
    
    if S[i][j] != ".":
      continue
    
    # 周囲８マスの"#"の個数を数える
    for dx, dy in zip(DX, DY):
      
      # マス（i, j）の周囲のマスを、ni・njとする
      ni, nj = i + dx, j + dy
      
      # マスが盤面外の場合はスキップする
      if ni < 0 or ni >= H or nj < 0 or nj >= W:
        continue
      
      # "#"であれば１増やす
      if S[ni][nj] == "#":
        result[i][j] += 1
  
for row in result:
  print(*row, sep='')
