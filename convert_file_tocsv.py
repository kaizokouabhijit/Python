import pandas as pd

readfile = pd.DataFrame("./NSI_112_C_2022_03_L1.txt")

readfile.to_csv('./NSI_112_C_2022_03_L1.csv')

