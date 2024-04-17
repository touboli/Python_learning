def func():
    """
    这个函数用于解决当一群小朋友（数量为n）围坐一圈，从第k个（默认k=0）小朋友开始数数，从1开始数到m（默认
为3），数字为m的小朋友退出，然后下面的小朋友继续从1开始数，当一圈数完以后，第一个小朋友
接着最后一个小朋友的数字继续，一直到只剩下一个小朋友，请问最后一个留下的是开始编号为多少
的小朋友？
    """
    print("请输入小朋友的数量：")
    number = input("请输入小朋友的数量：")
    number = int(number)
    a = []
    count = 1
    index = 0
    for i in range(0, number-1):
        a.append(i)

    while len(a) > 1:
        for j in range(len(a)):
            if count == 3:
                a.remove(a[index])
                count = 1
            else:
                count += 1
                index += 1
            if index == len(a):
                index = 0
    print(a)

def func2(*args):
    """定义一个高阶函数，用于计算传入值（任意多个）的阶乘，并返回结果除以3余1的值。"""
    a = []
    
    for i in args:
        result = 1
        for j in range(1,i+1):
            result *= j
        if result % 3 == 1:
            a.append(result)
    print(a)
    return a

func2(1,2,3,4,5,6,7,8,9,10)
    





