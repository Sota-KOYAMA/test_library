import pandas as pd
from scipy.stats import norm
#標準正規分布表の数値を表示する
class NormalTable:
    def __init__(self):
        table = []
        for i in range(31):
            lst = []
            for j in range(10):
                x = round(i/10+j/100,2)
                lst.append(round(round(norm.cdf(x),4)-0.5,4))
            table.append(lst)
        table = pd.DataFrame(table, columns=[round(x/100,2) for x in range(10)], index=[round(x/10,2) for x in range(31)])
        self.table = table
    def show_table(self):
        display(self.table)
    def value(self, x):
        i = int(x*10)
        j = int(x*100%10)
        return self.table.iat[i, j]