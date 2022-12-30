# ------------------------------------------------------------------
# 入力：a b 
# ------------------------------------------------------------------
s = input().split() # リスト


# ------------------------------------------------------------------
# 入力：1 2
# ------------------------------------------------------------------
i = list(map(int, input().split())) # リスト


# ------------------------------------------------------------------
# 入力：
# N
# 1 2 3 → [1, 2, 3]
# ------------------------------------------------------------------
N = int(input())
i = list(map(int, input().split()))


# ------------------------------------------------------------------
# 入力：
# N
# a
# b
# ...
# s_N → ['a', 'b', 's_N']
# ------------------------------------------------------------------
N = int(input())
s = [input() for i in range(N)]


# ------------------------------------------------------------------
# 入力：abcdefg → ['a', 'b', 'c', 'd', 'e', 'f']
# ------------------------------------------------------------------
s = [s for s in input()]


# ------------------------------------------------------------------
# 入力：
# 3
# 1 2
# 3 4
# 5 6 → [[1, 2], [3, 4], [5, 6]]
# ------------------------------------------------------------------
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]


# ------------------------------------------------------------------
# グラフ
# ------------------------------------------------------------------
# 頂点数、辺数
N, M = map(int, input().split())

# グラフを定義
G = [[] for i in range(N)]

# 辺を受け取る
for i in range(M):
  u, v = map(int, input().split())
  
  u -= 1
  v -= 1
  
  G[u].append(v)
  G[v].append(u)


# ------------------------------------------------------------------
# 
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# 
# ------------------------------------------------------------------
