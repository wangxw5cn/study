def demo1():
    a = 1
    b = 2
    c = a + b
    return c


def demo2():
    symbol_exchange_map = {
        "IF2010": "CFFEX",
        "rb2101": "SHFE",
        "m2101": "DCE",
        "SR101": "CZCE",
    }

    exchange = symbol_exchange_map["IC2101"]
    return exchange


i = 0


def demo3():
    global i
    i += 1
    print(f"调用Demo3函数，第{i}次")
    demo3()
