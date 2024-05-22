from scipy.stats import norm

#正規分布の確率を求める
class NormalDistribution:
    def __init__(self, loc, scale, level=4):
        self.loc = loc
        self.scale = scale
        self.level = level
    def prob(self, l=None, r=None): #P(l<=X<=r)の確率を求める
        result = 0
        pl = norm.cdf(l, loc=self.loc, scale=self.scale) if l is not None else 0
        pr = norm.cdf(r, loc=self.loc, scale=self.scale) if r is not None else 1
        if level:
            return round(round(pr, self.level) - round(pl, self.level), self.level)
        else:
            return pr-pl