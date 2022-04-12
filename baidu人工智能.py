#baidu-aip  人工智能模块接口
#人工智能技术又称为ai技术，人工智能不是让机器像人一样有意识，这是误解。
#人工智能只是做了一系列的识别，其实人工智能核心的技术就是做各种识别，比如
#识别人像、识别音频、识别视频、识别图片，这些目前都是已经落地的人工智能识别的
#一部分
#语音唤醒--语音识别  其实就是将语音转换成字符串，匹配了之后，然后去执行对应的指令
#如果在自己的项目中用到了人工智能识别技术，不需要自己去编写算法，这个成本是非常高的
#因为除了编写人工智能算法还要编写对应的训练集，这需要花费大量的时间和经历，成本很大
#可以使用已经成熟的大厂开发的人工智能接口，比如百度在图像方向的人工智能做的好，科大讯飞在
#语音识别方向做的比较好
#百度ai网站https://ai.baidu.com/ai-doc/OCR/1k3h7y3db

#安装pip install baidu-aip 
#百度账号15985830143   zhang-he123456
from aip import AipOcr

#通过百度人工智能图片识别接口，实现读取图片中的文字功能
APP_ID = '25925746'
API_KEY = '4CofwU4wKHt37lr1bDesbefn'
SECRET_KEY = 'DLOm0SKNmvkCQQOKaijkUQ9ZTiVx7Wvv'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
      with open(filePath, "rb") as fp:
         return fp.read()
image = get_file_content(r"./images/paizhao.jpg")
res_image = client.basicGeneral(image)
print(res_image)
