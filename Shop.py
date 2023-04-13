class Shop:
    def __init__(self):
        stock = []
        self._stock = stock

    def warehouse_delivery(self, computer):
        self._stock.append(computer)

    def sell_computer(self, computer):
        self._stock.remove(computer)

    def get_computer(self):
        computers = []
        for pc in self._stock:
            computers.append(pc)

        return computers

    def print(self):
        for pc in self._stock:
            print(str(pc))
