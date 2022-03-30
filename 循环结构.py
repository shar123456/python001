#for循环 就是对序列进行遍历(包括  列表  字典 元组 集合)
#range(10)  可以生成一个0-9的序列
#range(5,10)  可以生成一个,5-9的序列
#range(5,10,2)  可以生成一个,5 7 9的序列
for i in range(10):
    print(i,end='')

#求和
sum=0
for i in range(0,101):
    sum+=i
print("0-100的和：",sum)
#求最大值
listTemp=[12,34,4,4543,55555]
maxTemp=listTemp[0]
for i in listTemp:
    if maxTemp<i:
        maxTemp=i
print("最大值为：",maxTemp)

#求最大值
listTemp2=[12,34,4,4233543,55555]
maxTemp2=listTemp2[0]
for i in range(0,len(listTemp2)-1):
    if maxTemp2<listTemp2[i]:
        maxTemp2=listTemp2[i]
print("最大值为：",maxTemp2)


#while 循环
i=0
while i<10:
    if(i==3):
        continue
    if(i==8):
        break
    print(i,end=',')
    i+=1