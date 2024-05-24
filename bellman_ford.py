import networkx as nx
import matplotlib.pyplot as plt
import heapq

def bellman_ford(G,s):
    n = nx.number_of_nodes(G)
    D = [float("inf")] * n
    D[s] = 0
    for i in range(n-1):
        D_new = D[:]
        for u, v, d in G.edges(data=True):
            D_new[u] = min(D_new[u], D[v] + d["weight"])
            D_new[v] = min(D_new[v], D[u] + d["weight"])
        D = D_new
    for u, v, d in G.edges(data=True):
        if D[v] > D[u]+d["weight"]:
            return (False, D)
            # return (False, D)
    return (True, D)