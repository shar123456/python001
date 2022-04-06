import time
from tushare import get_realtime_quotes
for x in range(5):
 print("我爱你中国！")
 time.sleep(1)
datas =get_realtime_quotes("600745")
print(datas)
