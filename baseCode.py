#python基础知识

#号是单行注释
 
'''3个点
 是多行注释，'''

a1=3 #整型
a2=3.14 #浮点型
a3='单引号字符串'
a4="双引号字符串"
a8=True #布尔类型
a9=None #空值
print(a9)
#转义字符
a5="Hello\tWorld" #\t为制表符
print(a5)
a6="Hello\nWorld" #\n为换行符
print(a6)
#如果不希望转义字符转义，那么在字符串前加r
a7=r"Hello\nWorld" #r为取消转义字符的作用,原样输出
print(a7)
# 查看值类型type()
print(type(a8))
#将字符串转换成整型 int() 其他的 str()  float() bool()
a11=int("11")

#运算符 包括  算术运算符  赋值运算符  关系运算符 逻辑运算符

