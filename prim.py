import networkx as nx
from make_graph import *
from heapq import heappop, heappush
def prim(G,s):
    # 未探索のノードを管理する集合を作成
    X = set(G.nodes)
    # 始点を取り除く
    X.remove(s)
    # 始点からの距離を管理するheapを作成
    H = []
    # 始点に隣接する辺をheapに入れていく
    for u,v,d in G.edges(s, data=True):
        heappush(H, (d["weight"],u,v))
    # 最小全域木の辺を管理するリストを作成
    result = []
    # 未探索ノードがなくなるまで処理を行う
    while X:
        # heapからもっとも始点からの距離が短い辺を取り出す
        c, i, j = heappop(H)
        # 探索済みの場合スキップする
        if j not in X:
            continue
        # 探索済みにする
        X.remove(j)
        # resultに辺を追加する
        result.append((i+1, j+1))
        # 探索済みにしたノードの周りの辺をheapに追加していく
        for u,v,d in G.edges(j, data=True):
            if v in X:
                heappush(H, (d["weight"]+c,u,v))
    # 結果を返す
    return result