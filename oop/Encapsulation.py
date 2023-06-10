class Computer:
    def __init__(self):
        self.__maxprice = 8090

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def sexMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

