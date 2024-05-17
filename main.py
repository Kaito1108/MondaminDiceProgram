import random
from datetime import timedelta, datetime

dice = ["モ", "ン", "ダ", "ミ", "ン", "ン"]
diceroll = []
count = 0
base_date = datetime(1, 1, 1)  # Update the year to a valid value
result = False

while not result:
    for i in range(6):
        diceroll.append(random.choice(dice))

        if diceroll[i] == dice[i] and i == 5:
            # Match
            result = True
            break
        elif diceroll[i] == dice[i]:
            # Roll Match
            print(diceroll)
            continue
        else:
            # No Match
            count += 1
            diceroll = []
            break

result_date = base_date + timedelta(days=count)

print()
print("-----------------------")
print("Match!!")
print("Result >>> " + str(count) + "日")
print(
    "計算結果 >>> "
    + str(result_date.year - 1)
    + "年"
    + str(result_date.month)
    + "月"
    + str(result_date.day)
    + "日"
)
print("-----------------------")
