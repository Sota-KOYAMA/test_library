# 最小全域木を求める
最小全域木を求めます。prim法より低速です。
## 使用例
```python
G = nx.read_weighted_edgelist('sample.edgelst', nodetype=int)
print(kruskal(G))
```
出力
```
[(1, 2), (1, 8), (8, 7), (2, 3), (7, 6), (3, 9), (3, 4), (6, 5)]
```