# 最小全域木を求める
最小全域木を求めます。kruskal法よりも高速に動きます。
## 使用例
```python
G = nx.read_weighted_edgelist('sample.edgelst', nodetype=int)
s = 0
print(prim(G, s))
```
出力
```
[(1, 2), (1, 8), (8, 7), (2, 3), (7, 6), (3, 9), (3, 4), (6, 5)]
```