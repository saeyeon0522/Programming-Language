import numpy as np
import pandas as pd

file = pd.read_csv("C:\\python_work\\apply.csv")


grp = file.groupby(["근무지역"], as_index=False).sum()
sortgrp = grp.sort_values(by="모집인원", ascending = False)
arr = np.array(sortgrp)
print("모집분야\t모집인원")
for i, j in arr:
    print(f"{i}\t{j}")
