# クラス
# pythonはjavaみたいにsetter, getterいらない
class Plant:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def is_expensive(self, threshold = 1000): # この1000はデフォルト値で、関数呼び出すときに引数で上書きできる
        return self.price >= threshold

if __name__ == "__main__":
    test = Plant("テスト", 100)
    print("plant.pyが実行されました:", test.name)
