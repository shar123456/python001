import requests  #安装 pip install requests
url="https://webfs.tx.kugou.com/202204081423/262ca2e398b1428c8adc234\
7ba4b2223/part/0/1735025/KGTX/CLTX001/09698719d79fe3c9607ef125d650dfe3.mp3"
#get() 向服务器发送get请求  .content 获取二进制数据 （.text 获取文本数据）
data=requests.get(url).content

#写人到本地
with open(r"./images/一千年以后.mp3", "wb") as fp:
    fp.write(data)