import csv
import pytz
from datetime import datetime

from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.object import BarData
from vnpy.trader.database import database_manager

CHINA_TZ = pytz.timezone("Asia/Shanghai")

with open("if_data.csv") as f:
    reader = csv.DictReader(f)

    bars = []
    for d in reader:
        dt = datetime.strptime(d["datetime"], "%Y-%m-%d %H:%M:%S")
        dt = CHINA_TZ.localize(dt)

        bar = BarData(
            symbol=d["symbol"],
            exchange=Exchange(d["exchange"]),
            interval=Interval.MINUTE,
            datetime=dt,
            open_price=d["open"],
            high_price=d["high"],
            low_price=d["low"],
            close_price=d["close"],
            volume=d["volume"],
            open_interest=d["open_interest"],
            gateway_name="DB"
        )
        bars.append(bar)

    database_manager.save_bar_data(bars)
    print(f"完成数据插入，起始点{bars[0].datetime}，结束点{bars[-1].datetime}，总数据量{len(bars)}")
