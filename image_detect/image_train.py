import get_train
from NeuralNetwork import NeuralNetwork
import numpy as np
import joblib


"""
    项目：宠物连连看——图像检测识别
    
    总结：训练效果很好
    
    关键：learning_rate学习率设置为0.1
    1.（图像不需要太大64×64就很好）
    2.（learning_rate=0.2时，无论该什么参数（图像大小、训练次数）训练结果都是“一塌糊涂”）
    
"""

# 训练集x
x = []
# 循环读取图片96张
for i in range(1, 97):
    # 获取图片arr数据
    arr = get_train.get_train_x(i)
    x.append(arr)

# 创建训练集y
arr = get_train.get_train_y()
y = arr

# 初始化神经网络（144， 150， 12）
layers = (64, 100, 12)
print(f"初始化神经网络{layers}...")
nn = NeuralNetwork(layers)
print("神经网络初始化完成...")
# 训练神经网络
nn.fit(x, y, 0.1, epochs=30000)
print("训练完成...")

# 保存训练模型
joblib.dump(nn, "train_model.m")