- 離散型確率
    - 一様分布
    uniform
    - 超幾何分布
    hypergeom
    - 二項分布
    binom
    - ポアソン分布
    poisson
- 連続型確率
    - 正規分布
    norm
    - 指数分布
    expon

### rvs (Random variates) 確率変数
記法：rvs(loc=0, scale=1, size=1, random_state=None)
確率変数は、確率的な法則に従って変化する値のことです。
指定したパラメータに基づいて、正規分布に従う確率変数（取り得る値）を、ランダムに指定した個数だけ生成します。
### pdf (Probability density function) 確率密度関数
記法：pdf(x, loc=0, scale=1)
確率密度は、定義された域内での確率変数Xの値の相対的な出やすさを表します。
平たく言えば、確率密度関数は、連続型のデータを引数にとると確率密度が算出される関数のことです。
### pmf (Probability mass function) 確率質量関数
記法：pmf(k, n, p, loc=0)
確率質量は、確率変数Xのとびとびの要素ごとの相対的な出やすさを表します。
平たく言えば、確率質量関数は、離散型のデータを引数にとると確率質量が算出される関数のことです。
### logpdf (Log of the probability density function) ログ確率密度関数
記法：logpdf(x, loc=0, scale=1)
ログ確率密度関数は、底をeとする確率密度の対数をとったものです。
### df (Cumulative distribution function) 累積分布関数
記法：cdf(x, loc=0, scale=1)
累積分布関数は、確率変数X
がある値x
以下となる確率を計算します。
記法：interval(alpha, loc=0, scale=1)
実際のデータから計算される経験分布では、平均値も標準偏差も常に未知のものです。標本から得られた平均値が、母集団における真の母数
に近似できているか本当はわかりません。
そこで、一定の確率のもとに母数
を含む区間を求めることを区間推定といいます。

```
ss.確率分布.関数
```
のように記述する
## 使用例
```python
from scipy.stats as ss
print(ss.norm.pdf(x=1, loc=4, scale=0.8))
```