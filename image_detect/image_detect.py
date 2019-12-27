import get_test
import numpy as np
import joblib
from tool.arr_to_str import arr_to_string

# 加载模型
nn = joblib.load("train_model.m")

# 文件路径
path = "C:/Users/hasee/Desktop/图片/test/"

# 获取测试集test_x
test_x = []
# 循环读取图片97张
for i in range(1, 97):
    # 获取图片arr数据
    arr = get_test.get_test_x(i, path)
    test_x.append(arr)

# 进行测试，得到结果predictions
predictions = []
for i in range(len(test_x)):
    o = nn.predict(test_x[i])
    # print(o)
    # print(np.argmax(o))
    predictions.append(np.argmax(o)+1)

# 读取name文件，获取对应的名字name，如：1：bear
# 得到name_map
with open(path+"name.txt", "r") as f_name:
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


# 将预测结果添加一行英文name
predictions = [predictions]
temp = []
for i in range(len(predictions[0])):
    temp.append(name_map[predictions[0][i]])
predictions.append(temp)

# 将结果写入result.txt文件
with open(path+"result.txt", "w") as f_result:
    f_result.write(arr_to_string(np.array(predictions)))

print(np.array(predictions))