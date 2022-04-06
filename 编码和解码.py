#在python3中，字符串的类型有两种，bytes  str
#str存储unicode类型    bytes存储byte类型
#字符串转换成byte类型 叫编码
#byte转换成字符串类型  叫解码

#字符串（unicode）转 byte   编码过程
a="我爱北京"
b=a.encode("utf-8")#默认是utf-8
print(b)


#byte转字符串（unicode）   解码过程  编码方式要和解码方式一致，也就是用utf-8编码的，解码的时候 也要用utf-8
astr=b.decode("utf-8")#默认是utf-8
print(astr)


