import networkx as nx
import matplotlib.pyplot as plt
import heapq
def dijkstra(G, s):
    D = [float('inf')]*nx.number_of_nodes(G)
    X = set(G.nodes)
    D[s] = 0
    H = []
    heapq.heappush(H, (0,s))
    while X:
        w, u = heapq.heappop(H)
        if u not in X:
            continue
        X.remove(u)
        for u,v,d in G.edges(u, data=True):
            if D[v] > D[u] + d["weight"]:
                D[v] = D[u] + d["weight"]
                heapq.heappush(H, (D[v], v))
    return D