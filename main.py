from plant import Plant

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

    
pot = Plant("ポトス", 500)
print(pot.name, pot.price)
print(pot.is_expensive())
print(pot.is_expensive(300))

p1 = Plant("ポトス", 500)
p2 = Plant("ポトス", 500)
print(id(p1), id(p2))
# 「id()が同じかどうか」で判定
print(p1 == p2)

target = "サボテン"
try:
    print(plants[target])
except KeyError:
    print(f"{target} は plants に存在しません")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0では割れません"
    except TypeError:
        return "数値以外では割れません"

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))

# スライス
name = "こういち"
print(name[0:2])
print(name[:2])
print(name[2:])
print(name[2])
print(name[-1])
print(name[-0])
print(name[::2])
print(name[::1])
print(name[::-1])

# 内包表記（list comprehension）
# 1. 全部の値段を1.1倍(消費税込み)にした新しいリストを作る
prices_with_tax = [value * 1.1 for value in plants.values()]
print(prices_with_tax)

# 2. 1000円以上の植物の「名前」だけを集めたリストを作る(前にforループで書いたやつの内包表記版)
expensive_names = [name for name, price in plants.items() if price >= 1000]
print(expensive_names)

# 3. 名前の文字数が3文字以上の植物名だけを集める
long_names = [name for name in plants.keys() if len(name) >= 3]
print(long_names)

# set(集合)
# 最大の特徴: 重複を持てない
my_plants = {"ポトス", "アスパラガスナナス", "モンステラ"}
friend_plants = {"サボテン", "ガジュマル", "ポトス"}

print(my_plants & friend_plants) #積集合
print(my_plants | friend_plants) #和集合
print(my_plants - friend_plants) #差集合

# set = 集合（重複不可）
# list = 可変配列（重複可）
# dict = map（キー＋値）

# 可変長引数
def show_prices(*plant_names):
    for name in plant_names:
        if name in plants:
            print(f"{name}: {plants[name]}円")
        else:
            print(f"{name}は見つかりません")

show_prices("モンステラ");
show_prices("モンステラ","ガジュマル");
