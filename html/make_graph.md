# ランダムグラフを作成する
ランダムなnetworkxのグラフを作成します
## 初期化
```python
mg = MakeGraph(n ,weighted=False, directed=False, connected=True)
```
n: ノード数
weighted: 重み付き
directed: 有向
connected: 連結
をそれぞれ指定します。
指定しない場合は単純無向連結グラフが作成されます。
## グラフを取り出す
```python
G = mg.graph
```
以上のように取り出してください
## write_file
```python
name = "sample.edgelist"
mg.write_file(name)
```
作成したグラフをファイルに書きします。
nameが名前のファイルが作成されます。
nameを省略した場合、random_n_graph.edgelistがファイル名になります。
既に同じサイズのedgelistがある場合上書きされるので複数作成する場合は名前を指定してください。
## show_graph
```python
mg.show_graph()
```
作成したグラフをmatplotlibで表示します。