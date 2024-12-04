def add(a, b):
    return a + b


def test():
    n = 1
    for i in [1, 2.0, -3, True, "test"]:
        try:
            m = add(i, n)
            print(m)
        except TypeError:
            print("调用add函数出错，错误数据", i)
        finally:
            print(f"{i}数据调用add计算结束")


def main():
    print("开始运行测试")
    test()
    print("测试运行结束")


main()
