import random
from datetime import timedelta, datetime

dice = ["モ", "ン", "ダ", "ミ", "ン", "ン"]
diceroll = []
count = int()
base_date = datetime(0, 1, 1)
result = ""

while True:
    for i in range(6):
        diceroll.append(random.choice(dice))
        print(diceroll)

        if diceroll[i] == dice[i] and i == 5:
            result = "Match"
            break
        elif diceroll[i] == dice[i]:
            print("Roll Match")
            continue
        else:
            print("Not Match")
            count += 1
            diceroll = []
            break

    if result == "Match":
        result_date = base_date + timedelta(days=count)

        print()
        print("-----------------------")
        print("Match!!")
        print("Result >>> " + str(count) + "日")
        print("計算結果 >>> " + str(result_date.year) + "年" + str(result_date.month) + "月" + str(result_date.day) + "日")
        print("-----------------------")
        break

