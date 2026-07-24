
x = 10
name = "こういち"

print(x)
print(name)

print(str(x) + name)
print(f"{name}さんの好きな数字は{x}")
print(x, name, sep="-")

plants = {"エバーフレッシュ": 20000, "アスパラガスナナス": 300, "ポトス": 500}
price = list(plants.values())
print(price)
print(plants["ポトス"])
plants["モンステラ"] = 8000
print(plants)
print(sum(price))


def min_max(numbers):
    return min(numbers), max(numbers)   # 実はtupleを返している

low, high = min_max([3, 1, 4, 1, 5])   # 複数変数に一気に代入(アンパック)
print(low, high)   # 1 5

target = "サボテン"

if target in plants:
    print(f"{target}はリストにあります。価格は{plants[target]}円です")
else:
    print(f"{target}はリストにありません。")


for key, value in plants.items():
    print(f"{key}: {value}円")

total = 0
i = 0
while i < len(price):
    total += price[i]
    i += 1
print(total)


total = 0
i = 0
for i in range(len(price)):
    total += price[i]
print(total)

# plants 辞書を使って、forループとif文だけ(関数はまだ使わない)で以下の2つを求めてください。

# 1.一番高い植物の名前と金額を見つけて表示する
# 2.1000円未満の植物が何個あるか(件数)を数えて表示する

# 1
max_price = 0
max_name = ""
for key, value in plants.items():
    if value > max_price:
        max_price = value
        max_name = key
print(max_name, max_price)

# 2
counter = 0
for value in plants.values():
    if value < 1000:
        counter += 1
print(counter)

# threshold = しきい値
def count_under(plants, threshold = 1000):
    counter = 0
    for value in plants.values():
        if value < threshold:
            counter += 1
    return counter

print(count_under(plants))
print(count_under(plants, 10000))

# クラス
# pythonはjavaみたいにsetter, getterいらない
class Plant:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def is_expensive(self, threshold = 1000): # この1000はデフォルト値で、関数呼び出すときに引数で上書きできる
        return self.price >= threshold
    
pot = Plant("ポトス", 500)
print(pot.name, pot.price)
print(pot.is_expensive())
print(pot.is_expensive(300))

p1 = Plant("ポトス", 500)
p2 = Plant("ポトス", 500)
print(id(p1), id(p2))
# 「id()が同じかどうか」で判定
print(p1 == p2)