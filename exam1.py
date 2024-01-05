class market: #定義市場類別
    def __init__(self, vegetable, weight, price): #定義建構子，有蔬菜、重量、價格
        #定義蔬菜、重量、價格的屬性
        self.vegetable = vegetable
        self.weight = weight 
        self.price = price

    def market_math(self): #定義副函式market_math,主要是根據重量的大小來對重量*價格後的價錢打折
        if self.weight>=100:
            return self.weight*self.price*0.5
        elif self.weight>=75:
            return self.weight*self.price*0.7
        elif self.weight>=50:
            return self.weight*self.price*0.9
        else:
            return self.weight*self.price
    def market_name(self): #定義副函式market_name,主要是根據蔬菜的名稱來對重量*價格後的價錢打折
        if self.vegetable == "青江菜":
            return self.weight*self.price*0.95
        elif self.vegetable == "大白菜":
            return self.weight*self.price*0.85
        elif self.vegetable == "高麗菜":
            return self.weight*self.price*0.75
    def market_price(self): #定義副函式market_price,主要是根據蔬菜原本的價格來對重量*價格後的價錢打折
        if self.price == 0.75:
            return self.weight*self.price*0.78
        elif self .price == 0.55:
            return self.weight*self.price*0.88
        elif self .price == 0.35:
            return self.weight*self.price*0.98
def main(): #主函式
    #定義三個和market類別符合的物件
    vegetable1= market("青江菜", 100, 0.75)  
    vegetable2= market("大白菜", 75 , 0.55)
    vegetable3= market("高麗菜", 50, 0.35)
    print("蔬菜= ", vegetable1.vegetable)
    print("價格= ", vegetable1.market_math()) #呼叫market_math這個副函式來計算價格
    print("蔬菜= ", vegetable2.vegetable)
    print("價格= ", vegetable2.market_math()) #呼叫market_math這個副函式來計算價格
    print("蔬菜= ", vegetable3.vegetable)
    print("價格= ", vegetable3.market_math()) #呼叫market_math這個副函式來計算價格
    print("蔬菜= ", vegetable1.vegetable)
    print("價格= ", vegetable1.market_name()) #呼叫market_name這個副函式來計算價格
    print("蔬菜= ", vegetable2.vegetable)
    print("價格= ", vegetable2.market_name()) #呼叫market_name這個副函式來計算價格
    print("蔬菜= ", vegetable3.vegetable)
    print("價格= ", vegetable3.market_name()) #呼叫market_name這個副函式來計算價格
    print("蔬菜= ", vegetable1.vegetable)
    print("價格= ", vegetable1.market_price()) #呼叫market_price這個副函式來計算價格
    print("蔬菜= ", vegetable2.vegetable)
    print("價格= ", vegetable2.market_price()) #呼叫market_price這個副函式來計算價格
    print("蔬菜= ", vegetable3.vegetable)
    print("價格= ", vegetable3.market_price()) #呼叫market_price這個副函式來計算價格
if __name__ == "__main__":
    main()
