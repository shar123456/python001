import time
import tushare #免费的财经接口包  #安装 pip install tushare
'''for x in range(5):
 print("我爱你中国！")
 time.sleep(1)'''


data =tushare.get_realtime_quotes("600745")#要联网状态才能获取到数据
print(data)
