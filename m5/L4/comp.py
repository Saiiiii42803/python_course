class Comp:
    def __init__(self):
        self.__max_price = 1000
    def sell(self):
        print("selling_price: ",self.__max_price)
    def set_max_price(self, price):
        self.__max_price = price


c1 = Comp()
c1.sell()
c1.set_max_price(500)
c1.sell()