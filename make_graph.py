import networkx as nx
import random
import matplotlib.pyplot as plt

#n頂点のグラフを作成。標準では単純無向連結グラフである
def add_weight(G):
    for u, v in G.edges():
        G.edges[u,v]["weight"] = random.randint(1,100)
    return G
def make_Graph(n ,weighted=False, directed=False, connected=True):
    if n<=50:
        p = 0.1
    elif n<=200:
        p = 0.05
    else:
        p = 0.02
    while True:
        G = nx.fast_gnp_random_graph(n, p)
        if nx.is_connected(G) and connected:
            break
        elif not (nx.is_connected(G) or connected):
            break
    if weighted:
        G = add_weight(G)
    return G

def show_graph(G, weighted=False):
    pos = nx.spring_layout(G)  # レイアウトの計算
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue")
    if weighted:
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

class MakeGraph:
    def __init__(self, n ,weighted=False, directed=False, connected=True):
        self.n = n
        self.weighted = weighted
        self.graph = make_Graph(n, weighted=weighted, directed=directed, connected=connected)
    def write_file(self, name=""):
        if not name:
            name = f"random_{self.n}.edgelist"
        if self.weighted:
            nx.write_weighted_edgelist(self.graph, name)
        else:
            nx.write_edgelist(self.graph, name, data=False)
    def show_graph(self):
        show_graph(self.graph, self.weighted)