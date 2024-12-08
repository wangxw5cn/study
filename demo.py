import json
import csv
from datetime import datetime

if (__name__ == "__main__"):
    now_time: str = str(datetime.now())
    dic0 = {}
    dic0["key1"] = "测试1"
    dic0["键名2"] = 398
    dic0['3'] = [1, 2, 3]
    dic0['time'] = now_time
    dic1 = {}
    dic1["key1"] = "测试5"
    dic1["键名2"] = 3958
    dic1['3'] = [1, 5, 3]
    dic1['time'] = now_time
    print(type(dic0), dic0)
    print(str(datetime.now().date()))
    print(str(datetime.now().time()))
with open("json_test.json", "w") as f:
    json.dump(dic0, f, indent=4)

with open("csv_test.csv", "w", encoding="UTF-8", newline="") as f:
    write_steam = csv.DictWriter(f, fieldnames=["key1", "键名2", "3", "time"])
    write_steam.writeheader()
    write_steam.writerow(dic0)
    write_steam.writerow(dic1)

print("全部记录完毕")
print(now_time)
