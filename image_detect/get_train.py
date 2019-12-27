import numpy as np
from PIL import Image
from tool import arr_to_str

# 文件路径path 1.jpg
path = "C:/Users/hasee/Desktop/图片/训练集/"

def get_train_x(i):
    """获取训练集x的arrary数组"""

    # 打开图片
    image = Image.open(path+f"{i}.jpg")
    # 图片缩放12×12，灰度处理
    image_gray = image.resize((8, 8), Image.ANTIALIAS).convert("L")
    # 获取图片数据
    image_arr = np.array(image_gray)
    # 图像数据转为一维数组
    image_arr = image_arr.flatten()
    # image_arr = image_arr.reshape(image_arr.shape[0]*image_arr.shape[1], )
    # 图像数组的值除以256
    image_arr = image_arr / 256

    return image_arr

def f_train_x(arr):
    """将训练集x写入文件"""

    # 打开写入的文件train_x.txt训练集x文件
    with open(path + "train_x.txt", "a") as f_train_x:

            # 将数据写入文件
            f_train_x.write(arr_to_str.arr_to_string(arr) + "\n")

            # 关闭文件f_train_x
            f_train_x.close()

    print("图片写入完成！！")

def get_train_y():

    # 数据集
    arr_train_y = []

    for i in range(1, 97):
        int_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        num = int((i-1) / 8)
        int_list[num] = 1
        arr_train_y.append(int_list)

    return np.array(arr_train_y)

def f_train_y(arr):
    """将训练集y写入文件"""

    # 打开写入的文件train_y.txt训练集y文件
    with open(path + "train_y.txt", "w") as f_train_y:

            # 将数据写入文件
            f_train_y.write(arr_to_str.arr_to_string(arr))

            # 关闭文件f_train_y
            f_train_y.close()

    print("数据写入完成！！")


if __name__ == "__main__":

    open(path + "train_x.txt", "w")
    # 循环读取图片96张
    for i in range(1, 97):
        # 获取图片arr数据
        arr = get_train_x(i)
        print(arr)
        # 将训练集x写入文件
        f_train_x(arr)

    # 创建训练集y
    arr = get_train_y()
    print(arr)
    # 将训练集y写入文件
    f_train_y(arr)


