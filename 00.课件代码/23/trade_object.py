class TradeData:
    symbol: str = ""
    datetime: str = ""
    direction: str = ""
    price: float = 0.0
    volume: float = 0.0
    size: int = 0

    def __init__(
        self,
        symbol: str,
        datetime: str,
        direction: str,
        price: float,
        volume: float,
        size: int
    ):
        self.symbol = symbol
        self.datetime = datetime
        self.direction = direction
        self.price = price
        self.volume = volume
        self.size = size

    def calculate_trading_value(self) -> float:
        """计算成交金额的对象方法"""
        value = self.price * self.volume * self.size
        return value

    def to_str(self) -> str:
        """"""
        text = (
            f"{self.datetime}：{self.direction} {self.symbol} "
            f"{self.volume}手@{self.price}"
        )
        return text


class StockTradeData(TradeData):

    def calculate_cash_change(self):
        """计算股票成交现金变化"""
        value = self.price * self.volume * self.size
        return value


# 调用父类参数
stock_trade = StockTradeData(
    "600036", "20200916 9:30:05", "买入", 40, 100, 1
)
print(stock_trade.to_str())

# 扩展子类方法
print("股票成交的现金变化为", stock_trade.calculate_cash_change())


class FuturesTradeData(TradeData):

    margin_rate = 0.0

    def __init__(
        self,
        symbol: str,
        datetime: str,
        direction: str,
        price: float,
        volume: float,
        size: int,
        margin_rate: float
    ):
        super().__init__(symbol, datetime, direction, price, volume, size)
        self.margin_rate = margin_rate

    def calculate_cash_change(self):
        """计算期货成交现金变化"""
        value = self.price * self.volume * self.size * self.margin_rate
        return value


# 扩展子类数据
futures_trade = FuturesTradeData(
    "IF2010", "20200916 9:31:05", "买入", 4000, 1, 300, 0.15
)

print("期货成交的现金变化为", futures_trade.calculate_cash_change())


# 检查类型
trade = TradeData("EURUSD", "20200916 9:45:01", "卖出", 1.3, 10000, 1)

