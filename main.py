
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
