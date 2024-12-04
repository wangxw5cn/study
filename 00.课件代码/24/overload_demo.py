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

    def write_trade_log(self, strategy_name: str) -> None:
        """"""
        print(f"{strategy_name}成交数据", self.to_str())


class StockTradeData(TradeData):

    def calculate_cash_change(self):
        """计算股票成交现金变化"""
        value = self.price * self.volume * self.size
        return value

    def write_trade_log(self, strategy_name: str) -> None:
        """"""
        print(f"{strategy_name}股票成交数据", self.to_str())


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

    def to_str(self) -> str:
        """"""
        cash_change = self.calculate_cash_change()

        text = (
            f"{self.datetime}：{self.direction} {self.symbol} "
            f"{self.volume}手@{self.price} "
            f"消耗保证金{cash_change}"
        )
        return text

    def write_trade_log(self, strategy_name: str) -> None:
        """"""
        print(f"{strategy_name}期货成交数据", self.to_str())


def print_strategy_trade_twice(trade: TradeData, strategy_name: str):
    trade.write_trade_log(strategy_name)
    trade.write_trade_log(strategy_name)
