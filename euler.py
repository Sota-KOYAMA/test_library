import networkx as nx

def euler(G):
    G_copy = G.copy()
    N = len(G_copy.nodes())
    into_num = [0]*N
    for u,v in G.edges():
        into_num[u] += 1
        into_num[v] += 1
    flg = True
    c = []
    for i in range(N):
        if into_num[i]%2 == 1:
            c.append(i)
    if len(c) == 0:
        pass
    elif len(c) == 2:
        flg = False
    else:
        return (False, [])
    cycle = []
    start = 0 if flg else c[0]
    stack = [start]
    while stack:
        u = stack[-1]
        if G_copy.edges(u):
            u,v = list(G_copy.edges(u))[0]
            G_copy.remove_edge(u,v)
            stack.append(v)
        else:
            cycle.append(stack.pop()+1)
    return ("perfect euler!" if flg else "quasi-euler!", cycle[::-1])