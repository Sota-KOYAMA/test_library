# 標準正規分布表の数値を表示する
標準正規分布表を表示します。
任意の値の数値を取得することもできます。
## 初期化
```python
nt = NormalTable()
```
## show_table
標準正規分布表を表示します。python環境だと動かないので、jupyter notebookで実行してください。
```python
nt.show_table()
```
## value
ある１点の値を表示します。
```python
print(nt.value(0.25))
```
## 使用例
```python
nt = NormalTable()
print(nt.value(1.25))
```
出力
```
0.3944
```