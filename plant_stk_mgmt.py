
plants = {}
cont_flg = 1

def add_plant(name, price):
    plants[name] = price
    print("植物在庫が追加されました")
    print(plants)

def search_plant(name):
    if name in plants:
        price = plants[name]
        print(f"{name}の価格は、{price}です")
    else:
        print(f"{name}は存在しません")

def show_plants():
    for name,price in plants.items():
        if price >= 1000:
            print(f"{name}: {price}")

def sum_all_plants():
    total_price = 0
    for price in plants.values():
        total_price += price
    print(f"合計：{total_price}円です")

while cont_flg == 1:
    print(
    """
    1. 追加
    2. 検索
    3. 一覧
    4. 合計金額
    5. 終了
    /n
    数字を入力してください
    """)

    num = input()

    match int(num):
        case 1:
            print("植物名と価格を登録します")
            print("植物名を入力してください")
            name = input()
            print("価格を入力してください")
            price = int(input())
            add_plant(name, price)
        case 2:
            print("検索したい植物名を入力してください")
            name = input()
            search_plant(name)
        case 3:
            print("1000円以上の植物をすべて表示します")
            show_plants()
        case 4:
            print("全植物の合計金額を表示します")
            sum_all_plants()
        case 5:
            print("プログラムを終了します")
            cont_flg = 0
        case _:
            print("1~5の半角数字で入力してください")

