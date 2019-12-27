import numpy as np
from PIL import Image
import struct

"""
    总结：是不是傻！！！
    print(numpy, file=f)    ****************** 打印到文件 ******************
"""

def arr_to_string(arr):
    """将数组转化为字符串"""

    # 最终赋值的str
    str = ""
    # arr的shape
    dimension = arr.shape
    # 进入了第i维
    i = 0
    # 维度数n
    n = len(dimension)

    # 显示当前数组的shape
    # print(f"当前arr数组的shape：{dimension}")

    # 调用递归函数cycle(n, i, arr, dimension)，进行转化
    str = str + cycle(n, i, arr, dimension)

    # 返回str
    return str

def cycle(n, i, arr, dimension):
    """调用递归函数，进行多维的“级联式”转化"""

    str = ""

    if n == 1:
        str = str + '['
        for k in range(dimension[i]):
            if k == 0:
                str = str + f"{arr[k]}"
            else:
                str = str + f",{arr[k]}"
        str = str + ']'
    else:
        str = str + '['
        for k in range(dimension[i]):
            if k != 0:
                str = str + ','
            str = str + cycle(n-1, i+1, arr[k], dimension)
        str = str + ']'

    # 返回str
    return str


if __name__ == "__main__":

    image = Image.open("C:/Users/11097/Desktop/图片/训练集 - 副本/9.jpg")
    image_gray = image.resize((10, 10), Image.ANTIALIAS).convert("L")
    image_gray.show()
    arr_image = np.array(image.getdata())
    arr_image_gray = np.array(image_gray.getdata())
    print(arr_image)
    print(arr_image_gray)

    # str_image = arr_to_string(arr_image)
    # str_image_gray = arr_to_string(arr_image_gray)
    # print(str_image)
    # print(str_image_gray)

    # with open("C:/Users/11097/Desktop/图片/训练集 - 副本/test2.txt", 'w') as f:
    #     f.write(str)