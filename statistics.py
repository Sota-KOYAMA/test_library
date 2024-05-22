import numpy as np
import pandas as pd

# 代表値を求める
def statistics(lst):
    def mode(arr):
        unique, freq = np.unique(arr, return_counts=True)
        mode = unique[np.argmax(freq)]
        return mode
    arr = np.array(lst)
    index = ["平均値", "標本分散", "普遍分散", "標準偏差", "最頻値", "中央値"]
    result = [arr.mean(), arr.var(ddof=0), arr.var(ddof=1), arr.std(), mode(arr), np.median(arr)]
    return pd.Series(data=result, index=index)