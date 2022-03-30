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
        i+=1
        continue
    if(i==8):
       
        break
    print(i,end=',')
    i+=1

#模拟银行存取款
card1="0001"
pwd1="123456"
balance1=10000
card2="0002"
pwd2="123456"
balance2=10000
while(True):
    print("欢迎来到python银行")
    card=input("请输入卡号:")
    pwd=input("请输入密码:")
    ban=0
    if card==card1 and pwd==pwd1:
        ban=balance1
    elif card==card2 and pwd==pwd2:
        ban=balance2
    else:
        print("卡号和密码输入错误,请重新输入")
        continue
    while(True):
       num= input("请输入要办理的业务:1.存款 2.取款 3.退卡")
       if num=="1":
           inn=float(input("请输入存款金额:"))
           if inn<=0:
               print("存款金额请大于0.")
               continue
           else:
                ban=ban+inn
                print("存款成功,存入:",inn,"余额:",ban)
                continue

       elif num=="2":
           out=float(input("请输入取款金额:"))
           if out>ban:
               print("余额不足.")
               continue
           else:
                ban=ban-out
                print("取款成功,取出:",out,"余额:",ban)
                continue
       elif num=="3":
           print("请收好卡片,欢迎下次再来.")
           break
       else:
           print("输入有误.")
           continue

