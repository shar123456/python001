#快递价格计算器
print("欢迎进入快递计算系统")
weight=int(input("请输入重量(kg):"))
addressNum=input("请输入地点编号(01.其他 02.东三省/宁夏/青海/海南 03.新疆/西藏 04.港澳台/国外):")
price=0
if weight>=3:
    if addressNum=="01":
        price=10+5*(weight-3)
    elif addressNum=="02":
        price=13+6*(weight-3)
    elif addressNum=="03":
        price=16+7*(weight-3)
    elif addressNum=="04":
        price=19+8*(weight-3)
    else:
        print("地点编号输入有误.")
elif weight<3 and weight>0:
    if addressNum=="01":
        price=10
    elif addressNum=="02":
        price=13
    elif addressNum=="03":
        price=16
    elif addressNum=="04":
        price=19
    else:
        print("地点编号输入有误.")
else:
     print("重量输入有误.")
print("您的需要支付的价格为",price,"元.")

