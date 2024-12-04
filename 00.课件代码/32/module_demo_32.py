def sum_even(n):
    result = 0
    for i in range(0, n, 2):
        # print(i)
        # assert(i % 2 == 1)
        result += i
    return result


# import datetime
# print("当前时间是", datetime.datetime.now())

# from datetime import *
# print("当前时间是", datetime.now())

# from datetime import datetime
# print("当前时间是", datetime.now())

print(f"当前片段代码运行所在的命名空间是{__name__}")


if __name__ == "__main__":
    n = sum_even(50)
    print("sum_even函数测试结果为", n)
