
plants = {}

print("""
      1. 追加
      2. 検索
      3. 一覧
      4. 合計金額
      5. 終了
      /n
      数字を入力してください
      """)

num = input()

match num:
    case 1:
        print("植物名と価格を入力してください")
        name = input()
        price = input()
        add_plant(name, price)
    case 2:
        print(2)
    case 3:
        print(3)
    case 4:
        print(4)
    case 5:
        print(5)
    case _:
        print("1~5の半角数字で入力してください")

def add_plant(name, price):
    plants[name] = price
    print("植物在庫が追加されました")
    print(plants)

