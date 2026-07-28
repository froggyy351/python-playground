
plants = {"エバーフレッシュ": 20000, "アスパラガスナナス": 300, "ポトス": 500, "モンステラ": 8000}
cont_flg = True

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
            print(f"{name}は、{price}円です")

def sum_all_plants():
    total_price = 0
    for price in plants.values():
        total_price += price
    print(f"合計は{total_price}円です")

while cont_flg == True:
    print(
    """
    1. 追加
    2. 検索
    3. 一覧
    4. 合計金額
    5. 終了
    数字を入力してください
    """)

    while True:
        try:
            num = int(input())
            break
        except ValueError:
            print("入力が正しくありません。1~5の半角数字で入力してください")

    match num:
        case 1:
            print("植物名と価格を登録します")
            while True:
                name = input("植物名を入力してください：").strip()
                if name:
                    break
            print("価格を入力してください")
            while True:
                try:
                    price = int(input())
                    break
                except:
                    print("半角数字で入力してください")
            add_plant(name, price)
        case 2:
            print("検索したい植物名を入力してください")
            while True:
                name = input("植物名を入力してください：").strip()
                if name:
                    break
            search_plant(name)
        case 3:
            print("1000円以上の植物をすべて表示します")
            show_plants()
        case 4:
            print("全植物の合計金額を表示します")
            sum_all_plants()
        case 5:
            print("プログラムを終了します")
            cont_flg = False
        case _:
            print("1~5の半角数字で入力してください")

