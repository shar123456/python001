
try:
    ex=Exception("抛出自定义异常.")
    raise ex #抛出异常
except Exception as e:
    print("出现错误,错误:",e)
else:
    print("没出现错误时，执行")
finally:
    print("无论错误还是正确,都会执行")