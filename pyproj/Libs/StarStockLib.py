import tushare
import  os
# 定义股票数据类
class StockData(object):
    stockName=""
    def __init__(self, code):		
        self.currentPrice = ""
        self.code = code
        self.desc = ""
		
class Stock(object):


        def __init__(self):
          
            stockCodeFile=open(os.path.abspath(r'Libs\stockCode.txt'),"r")
            self.CodeData=stockCodeFile.read()
            stockCodeFile.close()

        def __GetRealTimeData(self,StockDataList): #加双下划线，定义为私有方法，只能在类内部使用   
        # print(data)
        # print(type(data))#该data的数据类型是'pandas.core.frame.DataFrame'，不是python的数据类型，是第三方包pandas的数据类型
            result=""
            for StockDataTemp in StockDataList:
                dataT = tushare.get_realtime_quotes(StockDataTemp.code)  # 要联网状态才能获取到数据
                StockDataTemp.stockName = dataT.loc[0][0]  # 获取股票名字
                StockDataTemp.currentPrice = float(dataT.loc[0][3])  # 获取股票当前价格
                StockDataTemp.desc = "，"+StockDataTemp.stockName + \
                "："+str(StockDataTemp.currentPrice)
                result+= StockDataTemp.desc
            print(result[1:]); #从第一个字符串开始截取一直到最后

        def ShowStock(self):           
            stockCodeList=[]
           

            for temp in eval(self.CodeData):#eval将字符串转换成列表
                stockCodeList.append(StockData(temp))   
            Stock.__GetRealTimeData(self,stockCodeList)