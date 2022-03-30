#股票提醒系统
import tushare
import time

#定义一个获取股票实时牌价的函数
def GetRealTimeData(StockDataTemp):
	data =tushare.get_realtime_quotes(StockDataTemp.code)#要联网状态才能获取到数据
	#print(data)
	#print(type(data))#该data的数据类型是'pandas.core.frame.DataFrame'，不是python的数据类型，是第三方包pandas的数据类型
	StockDataTemp.stockName=data.loc[0][0]#获取股票名字
	StockDataTemp.currentPrice=float(data.loc[0][3])#获取股票当前价格
	StockDataTemp.desc="股票名："+StockDataTemp.stockName+"当前价格："+str(StockDataTemp.currentPrice)
	return StockDataTemp

#定义股票数据类
class StockData(object):
	def __init__(self,code,buypoint,salepoint):
		self.stockName=""
		self.currentPrice=""
		self.code=code
		self.desc=""
		self.buypoint=buypoint
		self.salepoint=salepoint

#定义一个main方法
def StarMain(StockCodes):
	for StockCode in StockCodes:
		GetStockData=GetRealTimeData(StockCode)
		if StockCode.currentPrice>=StockCode.salepoint:
		   print(StockCode.stockName,"已经到达卖点！")
		elif StockCode.currentPrice<=StockCode.buypoint:
		   print(StockCode.stockName,"已经跌到买点，赶紧筹集资金！")
		else:
		   print(GetStockData.desc)

i=0
while i<10:
	code1=StockData("600745",69.0,73.0)
	code2=StockData("603686",17.0,19.5)
	if i!=0:
		print(".........")
	StockCodeList=[code1,code2]
	StarMain(StockCodeList)  #通过这种改进，把代码按照功能写进函数中，达到了低耦合的效果。
	i=i+1                    #就是写好一个方法，其他的都可以调用，共同使用。
	time.sleep(2)
	