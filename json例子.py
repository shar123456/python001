#python中的字典类型，经常会和json进行相互的转换
#比如发送过来一个json对象，在python端就需要将其转换成字典类型来进行处理
#简单来说 json就是一个有特定结构的字符串

import json

#json转字典
j='{"city":"北京","name":"熊猫"}'
p=json.loads(j)
print(type(p))

#字典转json
dic={"city":"北京","name":"熊猫"}
jsonStr=json.dumps(dic,ensure_ascii=False)
print(type(jsonStr))