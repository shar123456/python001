#定义一个集合，有两种方式一种是花括号的形式，用花括号不能定义空集，因为会和字典冲突，字典可以用花括号定义空集；
#另外一种方式是用set([])的形式
#集合也是无序集
a={1,2,3,1,1,"star"}
b=set([2,3,4,5,6,"Queen"])

#集合的第一个用途是可以对列表去重复，如下：
listTemp=[1,1,1,2,2,3,3,3]
seta=set(listTemp)
print(seta)
#将集合转成列表
lista=list(seta)
print(lista)
#集合的第二个用途是可以进行运算
#差集
print(a-b) #得到{'star', 1}
#并集
print(a|b) #得到{1, 2, 3, 4, 5, 6, 'Queen', 'star'}
#交集
print(a&b)  #得到{2, 3}
#对称差集
print(a^b)  #得到{'star', 1, 4, 5, 6, 'Queen'}