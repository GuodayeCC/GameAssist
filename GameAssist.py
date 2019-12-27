import operator
from pymouse import PyMouse
import numpy as np
import win32gui
from PIL import ImageGrab, Image
import time
import joblib



class GameAssist:

    def __init__(self, wdname):
        """初始化"""

        self.image_path = "C:\\Users\\hasee\\Desktop\\图片\\test\\"

        # 小图标编号矩阵
        self.im2num_arr = []

        # 小图宽度
        self.im_width = 43

        # 截图位置
        self.scree_left_and_right_point = (557, 248, 1072, 592)

        # 初始化鼠标
        self.mouse = PyMouse()

        # 获取窗口句柄
        self.hwnd = win32gui.FindWindow(0, wdname)
        if not self.hwnd:
            print("窗口找不到，请确认窗口句柄：{%s}" %wdname)
            exit()

        # 窗口显示最前面
        win32gui.SetForegroundWindow(self.hwnd)

    def screenshot(self):
        """屏幕截图"""

        # 1、用grab函数截图，参数为左上角和右下角
        image = ImageGrab.grab(self.scree_left_and_right_point)
        image.save(self.image_path+"main.jpg")

        # 2、分切小图
        image_list = {}
        offset = self.im_width

        # 3、8行12列
        for x in range(8):
            image_list[x] = {}
            for y in range(12):
                # 计算每个小图的位置上、左、右、下
                top = x * offset
                left = y * offset
                right = (y + 1) * offset
                bottom = (x + 1) * offset

                # 用 图像.crop() 函数切割成小图标
                im = image.crop((left, top, right, bottom))
                im.save(self.image_path+f"{x*12+y+1}.jpg")

                # 将切好的小图标存入对应的位置
                image_list[x][y] = im

        return image_list

    def image2num(self, image_list):
        """将图标矩阵转换成数字矩阵"""

        # 创建全零矩阵 和 空的一维数组
        arr = np.zeros((10, 14), dtype=np.int32)

        # 加载图像检测模型
        nn = joblib.load("image_detect/train_model.m")

        # 检测图像，得到结果值
        for row in range(len(image_list)):
            for col in range(len(image_list[0])):
                # 图像处理
                image_test = self.image_gray(image_list[row][col])
                # 图像检测得到数值num
                num = nn.predict(image_test)
                # 将数值写入arr中
                arr[row+1][col+1] = np.argmax(num)+1

        self.im2num_arr = arr
        return arr

    def image_gray(self, image):
        """将图像转为神经网络输入数据"""

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






    # 判断矩阵是否全为0
    def isAllZero(self, arr):
        for i in range(1, 9):
            for j in range(1, 13):
                if arr[i][j] != 0:
                    return False
        return True

    # 是否为同行或同列且可连
    def isReachable(self, x1, y1, x2, y2):
        # 1、先判断值是否相同
        if self.im2num_arr[x1][y1] != self.im2num_arr[x2][y2]:
            return False

        # 1、分别获取两个坐标同行或同列可连的坐标数组
        list1 = self.getDirectConnectList(x1, y1)
        list2 = self.getDirectConnectList(x2, y2)
        # print(x1, y1, list1)
        # print(x2, y2, list2)

        # exit()

        # 2、比较坐标数组中是否可连
        for x1, y1 in list1:
            for x2, y2 in list2:
                if self.isDirectConnect(x1, y1, x2, y2):
                    return True
        return False

    # 获取同行或同列可连的坐标数组
    def getDirectConnectList(self, x, y):

        plist = []
        for px in range(0, 10):
            for py in range(0, 14):
                # 获取同行或同列且为0的坐标
                if self.im2num_arr[px][py] == 0 and self.isDirectConnect(x, y, px, py):
                    plist.append([px, py])

        return plist

    # 是否为同行或同列且可连
    def isDirectConnect(self, x1, y1, x2, y2):
        # 1、位置完全相同
        if x1 == x2 and y1 == y2:
            return False

        # 2、行列都不同的
        if x1 != x2 and y1 != y2:
            return False

        # 3、同行
        if x1 == x2 and self.isRowConnect(x1, y1, y2):
            return True

        # 4、同列
        if y1 == y2 and self.isColConnect(y1, x1, x2):
            return True

        return False

    # 判断同行是否可连
    def isRowConnect(self, x, y1, y2):
        minY = min(y1, y2)
        maxY = max(y1, y2)

        # 相邻直接可连
        if maxY - minY == 1:
            return True

        # 判断两个坐标之间是否全为0
        for y0 in range(minY + 1, maxY):
            if self.im2num_arr[x][y0] != 0:
                return False
        return True

    # 判断同列是否可连
    def isColConnect(self, y, x1, x2):
        minX = min(x1, x2)
        maxX = max(x1, x2)

        # 相邻直接可连
        if maxX - minX == 1:
            return True

        # 判断两个坐标之间是否全为0
        for x0 in range(minX + 1, maxX):
            if self.im2num_arr[x0][y] != 0:
                return False
        return True

    # 点击事件并设置数组为0
    def clickAndSetZero(self, x1, y1, x2, y2):
        # print("click", x1, y1, x2, y2)

        # (557, 248, 1072, 592)
        # 原理：左上角图标中点 + 偏移量
        p1_x = int(self.scree_left_and_right_point[0] + (y1 - 1) * self.im_width + (self.im_width / 2))
        p1_y = int(self.scree_left_and_right_point[1] + (x1 - 1) * self.im_width + (self.im_width / 2))

        p2_x = int(self.scree_left_and_right_point[0] + (y2 - 1) * self.im_width + (self.im_width / 2))
        p2_y = int(self.scree_left_and_right_point[1] + (x2 - 1) * self.im_width + (self.im_width / 2))

        time.sleep(0.2)
        self.mouse.click(int(p1_x/5*4), int(p1_y/5*4))
        time.sleep(0.2)
        self.mouse.click(int(p2_x/5*4), int(p2_y/5*4))

        # 设置矩阵值为0
        self.im2num_arr[x1][y1] = 0
        self.im2num_arr[x2][y2] = 0

        print("消除：(%d, %d) (%d, %d) 位置：(%f, %f) (%f, %f) " % (x1, y1, x2, y2, p1_x, p1_y, p2_x, p2_y))
        # exit()

    # 程序入口、控制中心
    def start(self):

        # 1、先截取游戏区域大图，然后分切每个小图
        image_list = self.screenshot()

        # 2、识别小图标，收集编号
        self.image2num(image_list)

        print(self.im2num_arr)

        # 3、遍历查找可以相连的坐标
        while not self.isAllZero(self.im2num_arr):
            for x1 in range(1, 9):
                for y1 in range(1, 13):
                    if self.im2num_arr[x1][y1] == 0:
                        continue

                    for x2 in range(1, 9):
                        for y2 in range(1, 13):
                            # 跳过为0 或者同一个
                            if self.im2num_arr[x2][y2] == 0 or (x1 == x2 and y1 == y2):
                                continue
                            if self.isReachable(x1, y1, x2, y2):
                                self.clickAndSetZero(x1, y1, x2, y2)

    def arr_to_name(self, arr):
        """工具：将图片数字编号-->名字name"""

        # 读取name文件，获取对应的名字name，如：1：bear
        # 得到name_map
        with open(self.image_path + "name.txt", "r") as f_name:
            name_map = {}
            while True:
                # 读取一行
                name_line = f_name.readline()
                # 去除开头结尾空格" "
                name_line = name_line.strip()
                # 去除换行"\n"
                name_line = name_line.rstrip('\n')

                if name_line and name_line != "":
                    name_split = name_line.split(":", 1)
                    name_key = int(name_split[0])
                    name_value = name_split[1]
                    name_map[name_key] = name_value
                else:
                    break

        names = [['']*12 for i in range(8)]
        for i in range(1, len(arr)-1):
            for j in range(1, len(arr[0])-1):
                names[i-1][j-1] = name_map[arr[i][j]]

        return np.array(names)

if __name__ == "__main__":

    wdname = "宠物连连看经典版2小游戏,在线玩,4399小游戏 - 360安全浏览器 10.0"

    demo = GameAssist(wdname)
    demo.start()
    # image_list = demo.screenshot()
    # arr = demo.image2num(image_list)
    # print(demo.arr_to_name(arr))