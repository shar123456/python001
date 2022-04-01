#文件读写  就是IO操作，可以对磁盘进行持久化文件的读取和写入
fr=open(r"./files/test1.txt","r",encoding="utf-8") #r --read 读取  是文件的句柄
data=fr.read()
#data=fr.readline()#按行读取
#data=fr.readlines()#按行读取所有   得到一个列表
print(data)
fr.close() #关闭文件 文件操作完毕后，一定要关闭IO资源

#如果是读取大文件 那就要用for循环,这种方式可以大大减少内存的消耗
'''for i in fr:
    print(i)
fr.close()'''

#文件写入
'''fw=open(r"./files/test1.txt","w",encoding="utf-8") #w --write写入  是文件的句柄
fw.write("我是写入的文本")  #如果文件存在就重新写入，覆盖之前的内容。如果文件不存在，则会新建一个文件
fw.close()'''

fw1=open(r"./files/test1.txt","a",encoding="utf-8") #a --append追加写入，不会覆盖原有内容  是文件的句柄
fw1.write("我是写入的文本")  
fw1.close()

#读取二进制文件  图片 视频 音频  excel  word文档  都是二进制文件
fbr=open(r"./images/bg1.jpg","rb")
fbr_data=fbr.read()
print(fbr_data)
fbw=open(r"./images/bg3.jpg","wb") #实现了文件的复制 粘贴
fbw.write(fbr_data)
fbr.close()
fbw.close()