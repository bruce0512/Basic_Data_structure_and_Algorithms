#定義陣列兩元素交換#
def switch(array, a, b):
    value1 = array[a]
    value2 = array[b]
    array[a] = value2
    array[b] = value1
    return

#定義快速排序法#
def quicksort(array, start, end):

    #如果起點小於或等於終點，直接回傳陣列#
    if start >= end:
        return

    #宣告左指標#
    left_pointer_index = start
    #宣告右指標#
    right_pointer_index = end
    #宣告基準點#
    pivot = array[start]

    #移動指標#
    while left_pointer_index != right_pointer_index:

        #尋找比右指標小的值#
        while array[right_pointer_index] >= pivot and right_pointer_index > left_pointer_index:
            right_pointer_index -= 1
        #尋找比佐指標大的值#
        while array[left_pointer_index] <= pivot and right_pointer_index > left_pointer_index:
            left_pointer_index += 1
        #互換左右指標的值#
        if right_pointer_index > left_pointer_index:
            switch(array, right_pointer_index, left_pointer_index)

    #當左右指標的值相同時，該值與基準點互換#
    switch(array, array.index(pivot), left_pointer_index)

    #列印出交換過程
    print("過程")
    print(array)

    #處理後續子陣列#
    pivot_index = array.index(pivot)
    quicksort(array, start, pivot_index-1)
    quicksort(array, pivot_index+1, end)

    #回傳排序好的陣列#
    return array

#主程式#
if __name__ == "__main__":

    #排序課程中的範例#
    data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
    print("課程範例 : ", data)
    print('\n','-------------------------------------','\n')
    quicksort(data, 0, len(data)-1)
    print('\n','-------------------------------------','\n')
    print("排序結果: ", data)

    print('\n', '##############################################','\n')


    #排序1~100隨機的20個數字#
    import random
    nums = random.sample(range(1, 101), 20)
    print("隨機數字 : ", nums)
    print('\n','-------------------------------------','\n')
    quicksort(nums, 0, len(nums)-1)
    print('\n','-------------------------------------','\n')
    print("排序結果: ", nums)


# PS C:\Users\bruce\vscode\code\Basic_Data_structure_and_Algorithms> & C:/Users/bruce/AppData/Local/Programs/Python/Python38/python.exe c:/Users/bruce/vscode/code/Basic_Data_structure_and_Algorithms/hw3_quick_sort.py
# 課程範例 :  [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

#  ------------------------------------- 

# 過程
# [3, 25, 8, 13, 33, 119, 54, 84, 67, 41]
# 過程
# [3, 25, 8, 13, 33, 119, 54, 84, 67, 41]
# 過程
# [3, 13, 8, 25, 33, 119, 54, 84, 67, 41]
# 過程
# [3, 8, 13, 25, 33, 119, 54, 84, 67, 41]
# 過程
# [3, 8, 13, 25, 33, 41, 54, 84, 67, 119]
# 過程
# [3, 8, 13, 25, 33, 41, 54, 84, 67, 119]
# 過程
# [3, 8, 13, 25, 33, 41, 54, 84, 67, 119]
# 過程
# [3, 8, 13, 25, 33, 41, 54, 67, 84, 119]

#  -------------------------------------

# 排序結果:  [3, 8, 13, 25, 33, 41, 54, 67, 84, 119]

#  ##############################################

# 隨機數字 :  [90, 34, 37, 30, 20, 43, 38, 59, 94, 28, 24, 9, 89, 7, 93, 10, 58, 22, 95, 92]

#  -------------------------------------

# 過程
# [10, 34, 37, 30, 20, 43, 38, 59, 22, 28, 24, 9, 89, 7, 58, 90, 93, 94, 95, 92]
# 過程
# [9, 7, 10, 30, 20, 43, 38, 59, 22, 28, 24, 37, 89, 34, 58, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 30, 20, 43, 38, 59, 22, 28, 24, 37, 89, 34, 58, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 22, 20, 24, 28, 30, 59, 38, 43, 37, 89, 34, 58, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 59, 38, 43, 37, 89, 34, 58, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 59, 38, 43, 37, 89, 34, 58, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 34, 38, 43, 37, 58, 59, 89, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 34, 38, 43, 37, 58, 59, 89, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 34, 37, 38, 43, 58, 59, 89, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 34, 37, 38, 43, 58, 59, 89, 90, 93, 94, 95, 92]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 34, 37, 38, 43, 58, 59, 89, 90, 92, 93, 95, 94]
# 過程
# [7, 9, 10, 20, 22, 24, 28, 30, 34, 37, 38, 43, 58, 59, 89, 90, 92, 93, 94, 95]

#  -------------------------------------

# 排序結果:  [7, 9, 10, 20, 22, 24, 28, 30, 34, 37, 38, 43, 58, 59, 89, 90, 92, 93, 94, 95]
