print("打印============================")
print("hello python")

print("变量类型========================")
counter = 100
print(counter)
print('字符串hahaha')
# string类型str[2:6:2] 第一个参数，是字符串起点，第二个参数：终点，第三个参数：步长
str = "checkout"
print(str[2:6:2])
# 列表截取，类似字符串截取，不同的是，字符串截取出来是字符串，列表截取出来还是列表(左闭右开)
list = ['c', 'h', 'e', 'c', 'k', 'o', 'u', 't']
print(list[2:6:2])
print(list[1:3])
list.append('我是后来的')
print(list)
# python元组 元组不能二次赋值，相当于只读列表
tuple = ('runoob', '786', 2.23, 'join', 70.2)
# 字典（dictionary）基本用法,
dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'
print(dict)
print(dict.keys())
print(dict.values())
# python 类型转换
a = 0
print(int(a))
print(float(a))
# if基本语法
flag = False
name = "java"
if name == 'python':  # 判断变量是否为python
    print(name)
elif name == 'java' and flag == False:
    print(name + flag.__str__())
else:
    print(name)
