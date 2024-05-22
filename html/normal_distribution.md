# 正規分布の確率を求める
任意の範囲の確率を求めます。
## 初期化
```python
loc = 2.5
scale = 4
level = 3
nd = NormalDistribution(loc, scale, level)
```
ここで、locは平均、scaleは標準偏差、levelは小数点以下を丸める位置です。levelは省略可能であり、省略した場合は少数第4位まで表示します。すべて表示したい場合はlevel=Noneとしてください。
## prob
```python
print(nd.prob(l=-0.4,r=2))
```
P(l<=x<=r)を求めます。l, rのどちらかは省略することが可能です。省略した場合、端まで含めて計算することになります。
## 使用例
```python
loc = 1
scale = 2
level = 4
nd = NormalDistribution(loc, scale, level)
nd.prob(1,2)
```
出力
```
0.1915
```