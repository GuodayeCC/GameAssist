"""文件模式mode：
r：只读， 指针在头           ， 不能写
w：只写， 指针在头， 创建文件， 不能读   （覆盖）
a：只写， 指针在尾， 创建文件， 不能读  （追加）

r+:读写， 读指针在头，写指针在尾  (追加）   (读写时：推荐使用)
w+:读写， 指针在头， 创建文件   （覆盖）
a+:读写， 指针在尾， 创建文件  （追加）

（覆盖：打开文件时，文件内容就消失）
"""

name_list = ["bear", "cat", "chicken", "dog", "elephant", "frog", "mouse",
             "penguin1", "penguin2", "rabbit1", "rabbit2", "tiger"]
with open("C:\\Users\\11097\\Desktop\\图片\\训练集\\name.txt", 'w') as file:
    n = 0
    for i in range(1, 97):
        if i % 8 == 1:
            n += 1
        file.write(f"{i}:{n}:{name_list[n-1]}\n")

'''
# 以二进制、读、写覆盖的mode打开文件test2.txt
with open("C:/Users/11097/Desktop/图片/训练集 - 副本/test2.txt", 'wb+') as f:
    # utf-8编码 ‘我’对应的16进制
    # E68891

    # 输出原文件数据
    print(f.read())

    # byte = struct.pack('B', 2)
    # byte = struct.pack('B', 2)
    # 创建二进制数据，可以连续，单一
    bytes = bytearray([230, 136, 145])
    # 输出数据检验
    print(bytes)

    # 写入文件中
    f.write(bytes)

    # 关闭文件
    f.close()
'''