import pandas as pd
import xlrd

#
#IO: input / output理解为:文件的读与写
#'https : / /pandas.pydata.org/pandas-docs/version/1.0.1/user_guide/io.html '


#读取粘贴板数据
df=pd.read_clipboard()
print(df)
print("------")
#读取数据
#read_csv可读取txt以及csv文件
df1=pd.read_csv('../files/iotest.txt')
print(df1)
print("------")
#read_excel读取excel数据
df2=pd.read_excel('../files/iotest.xlsx',engine='openpyxl')
print(df2)


##输出数据
#to_exce,to_csv,to_dict,to_html
df2.to_excel("../files/df3.xlsx",sheet_name="pysheet",header=True,index=True)#header为true代表输出头信息，index为true代表输出行索引
df2.to_csv("../files/df3.csv",header=True,index=True)
df2.to_dict()
df2.to_html("../files/df3.html")