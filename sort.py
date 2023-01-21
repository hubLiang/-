'''
实现排序、查找
'''
#计算成绩平均值
def averge(l: list):
    i = 0
    sum = 0
    for i in range(len(l)):
        sum += l[i].score
    return sum / len(l)

# 排序:按成绩
    #降序
def sort_byscore_des(arr:list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][4] < arr[j + 1][4]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
    #升序
def sort_byscore_asc(arr:list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][4] > arr[j + 1][4]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#查找
def binsearch(arr:list,target:int)->int:
    left=1
    right=len(arr)
    while left+1!=right:
        middle=(left+right)//2
        if arr[middle][4]<target:
            left=middle
        elif arr[middle][4]>target:
            right=middle
        else:
            return middle
