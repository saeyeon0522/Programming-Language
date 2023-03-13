import numpy as np
import pandas as pd


file1 = pd.read_csv("C:\\python_work\\convience_1.csv")
file2 = pd.read_csv("C:\\python_work\\convience_2.csv")


filecombine = pd.concat([file1, file2])
df = filecombine

df["급여"] = df["시급"] * df["근무시간"]
aaa=df.sort_values(by = "급여", ascending = False)
aaa.to_csv("C:\\python_work\\21102054_임새연_test1.csv")
