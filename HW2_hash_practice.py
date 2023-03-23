# 存取檔案
file = open("./hw2_data.txt", "r")
data = file.readlines()

# 去除字尾的\n
for i in range(len(data)):
    data[i] = data[i].strip("\n")

# 製作雜湊
data.sort()
data_hash = {}
for i in range(len(data)):
    if data[i] in data_hash:
        data_hash[data[i]] += 1
    else:
        data_hash[data[i]] = 1

# 列印結果
print(f'總共有{len(data_hash)}個不重複的英文字')
for key, value in data_hash.items():
    print(f'{key} : {value}個')




# PS C:\Users\bruce\vscode\code\Basic_Data_structure_and_Algorithms> & C:/Users/bruce/AppData/Local/Programs/Python/Python38/python.exe c:/Users/bruce/vscode/code/Basic_Data_structure_and_Algorithms/hw2_data_txt.py
# 總共有10個不重複的英文字
# Burger : 196個
# Cheese : 234個
# Coke : 145個
# Fries : 76個
# Pho : 19個
# Pizza : 83個
# Potato : 3個
# Rib : 33個
# Steak : 46個
# Taco : 57個
