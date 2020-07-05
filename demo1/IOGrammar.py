
# 读模式，encoding表示编码集，根据文件的实际保存编码进行获取数据，对我们而言，更多是utf-8
f = open("Readable.txt", mode='r', encoding="utf-8")
# 1.read()将文件中的内容全部读取出来，弊端占内存，如果文件过大，容易导致内存崩溃
content = f.read()
print(content)
print(f.encoding)
f.close()

# 2.readline()一次读取一行数据，注意每次读取都会有一个\n存在，需要用strip()去掉\n或空格
f = open("Readable.txt", mode='r', encoding="utf-8")
content1 = f.readline()
content2 = f.readline()
print(content1.strip())
print(content2.strip())
f.close()

# 3.readlines()将每一行形成一个元素，放到一个列表中
print("readlines()==========================")
f = open("Readable.txt", mode='r', encoding="utf-8")
list = f.readlines()
print(list)

for str in list:
    # 字符串非空判断，去除字符串首尾空格换行后，判断他的长度是否为0
    if len(str.strip()) != 0:
        print(str.strip())
f.close()

# 写模式 写的时候，如果没有文件，会创建文件，如果文件存在，删除原来内容，再写入新内容
print("============写模式============")
f = open("Writable.txt", mode="w", encoding="utf-8")
f.write("baby")
f.flush()
f.close()

# 追加（a，ab）
f = open("Writable.txt", mode="a", encoding="utf-8")
f.write("\nyou are beautiful")
f.flush()
f.close()

# 读写mode="r+" r+模式下. 必须是先读取. 然后再写入



