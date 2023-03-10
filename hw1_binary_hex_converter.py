##輸入小於255的數字##

num = 256
while num > 255:
    num = eval(input('輸入一個十進位的數字: '))
    if num <= 255:
        break
print('十進位:', num)

##轉為2進位##

# 計算出二進位數字
binary_num_2 = []
mod_num_2 = []
binary_num_2.append(num // (2**(7)))
mod_num_2.append(num % (2**(7)))

for i in range(7):
    binary_num_2.append(mod_num_2[i] // (2**(6-i)))
    mod_num_2.append(mod_num_2[i] % (2**(6-i)))

# 去除開頭的0

for j in range(len(binary_num_2)):
    if binary_num_2[0] == 0:
        binary_num_2.pop(0)
    else:
        break

# 列出數字
print('二進位: ', end='')
for k in range(len(binary_num_2)):
    print(binary_num_2[k], end='')


##轉為16進位##

bit_16 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
bit_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 計算出16進位數字
binary_num_16 = []
mod_num_16 = []
binary_num_16.append(num // (16**(1)))
mod_num_16.append(num % (16**(1)))
binary_num_16.append(mod_num_16[0] // (16**(0)))
mod_num_16.append(mod_num_16[0] % (16**(0)))

# 去除開頭的0

for j in range(len(binary_num_16)):
    if binary_num_16[0] == 0:
        binary_num_16.pop(0)
    else:
        break

# 將大於10的數字更換成字母

for j in range(len(binary_num_16)):
    binary_num_16[j] = bit_16[bit_2.index(binary_num_16[j])]

# 列出數字
print('')
print('16進位: ', end='')
for k in range(len(binary_num_16)):
    print(binary_num_16[k], end='')

    
    
    
    
 
# 輸出結果:   
# PS C:\Users\bruce\vscode\code> & C:/Users/bruce/AppData/Local/Programs/Python/Python38/python.exe c:/Users/bruce/vscode/code/converter.py
# 輸入一個十進位的數字: 234
# 十進位: 234
# 二進位: 11101010
# 16進位: EA

