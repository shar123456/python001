import tushare #免费的财经接口包  #安装 pip install tushare
import time
i=0
while(i<20):
     data =tushare.get_realtime_quotes("600745")#要联网状态才能获取到数据
     #print(data)
     #print(type(data))#该data的数据类型是'pandas.core.frame.DataFrame'，不是python的数据类型，是第三方包pandas的数据类型
     stoclName=data.loc[0][0]#获取股票名字
     currentPrice=float(data.loc[0][3])#获取股票当前价格
     print("股票名：",stoclName,"当前价格：",currentPrice)
     buypoint=73.0
     salepoint=68.0
     if(currentPrice>=buypoint):
          print("已经到了买点！")
     elif(currentPrice<=salepoint):
          print("已经到了卖点！")
     i=i+1
     time.sleep(2)