import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.parser import parse


# df = pd.read_excel(r"ACD019600\data\test.xlsx", engine="openpyxl", sheet_name=0, index_col=1)
# print(df)
# print(df.shape)
# print(df.info())
# print(df.describe())

# df = pd.DataFrame([[20, 5000, 2], [25, 8000, 3], [30, 9000, 3], [28, 7000, 2]], columns=["Age", "income", "members"])
# stat = df.describe()
# print(stat)
# df = pd.read_excel(r"ACD019600\data\test5.xlsx", engine="openpyxl", sheet_name=0)
# print(df.isnull())

# Chapter 6
# df = pd.read_excel(r"ACD019600\data\test6.xlsx", engine="openpyxl", sheet_name=0)
# print(df)
# print(df[["訂單編號", "客戶姓名"]])
# print(df.iloc[:, 1:4])

# Chapter 7
# df = pd.read_excel(r"ACD019600\data\test7.xlsx", engine="openpyxl", sheet_name="7-1")
# df["年齡"].replace(240, 33, inplace=True)
# print(df)
# df = pd.read_excel(r"ACD019600\data\test7.xlsx", engine="openpyxl", sheet_name="7-1b")
# print(df)
# df.replace(np.NaN, 0, inplace=True)
# print(df)
# df = pd.read_excel(r"ACD019600\data\test7.xlsx", engine="openpyxl", sheet_name="7.1.3 多對多取代")
# df.replace({240:32, 260:33, 280:34}, inplace=True)
# print(df)
# df = pd.read_excel(r"ACD019600\data\test7.xlsx", engine="openpyxl")
# df.sort_values(by=["年齡"], inplace=True)
# df.sort_values(by=["年齡"], inplace=True)
# print(df)
# df = pd.read_excel(r"ACD019600\data\test7.xlsx", engine="openpyxl")
# df["銷售ID"].rank(method="average", inplace=True)
#Typeerror: rank()
# print(df)
# df = pd.read_excel(r"ACD019600\data\test7.xlsx", engine="openpyxl")
# df.insert(2, "商品類別", ["cat1","cat2","cat3", "cat4","cat5"])
# print(df)

#Chap 9 時間序列
# print(datetime.now())
# print(datetime.now().year)
# print(datetime.now().month)
# print(datetime.now().day)
# print(datetime.now().weekday()+1)
# print(datetime.now().date())
# print(datetime.now().time())
# print(datetime.now().strftime('%Y-%m-%d'))
#字串格式轉換成時間格式
# str_time = "2021-05-20"
# print(type(str_time))
# time_fmt = parse(str_time)
# print(type(time_fmt))

#兩個時間之差
# diff = datetime(2021,5,20,11,39) - datetime(2021,5,17,8,0)
# print(diff)
# print(diff.days)
# print(diff.seconds)
# print(diff.seconds/3600)

#Chap 10 資料分組
# df = pd.read_excel(r"ACD019600\data\test10.xlsx", engine="openpyxl")
#print(df)
# print(df.groupby("客戶分類").count())
# print(df.groupby("客戶分類").sum())
# print(df.groupby(["客戶分類", "區域"]).sum())

#Chap 11 多表拼接
print("The end.")
