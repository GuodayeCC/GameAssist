import numpy as np
from PIL import Image


def get_test_x(i, path):
    """获取测试集x的arrary数组"""

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