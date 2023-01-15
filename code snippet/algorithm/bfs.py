from queue import Queue

def bfs(G, s):
    Q = Queue()
    dist = [-1] * len(G)

    Q.put(s)
    dist[s] = 0

    while not Q.empty():
        # キューから頂点vを取り出す
        v = Q.get()
        
        for v2 in G[v]:
            if dist[v2] != -1:
                continue
            
            # v2を新たにキューに追加
            Q.put(v2)

            # v2のdistを修正
            dist[v2] = dist[v] + 1
    
    return dist

# 入力
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)

# 実行   
print(bfs(G, 0))
