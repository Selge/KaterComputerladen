from Computer import Computer


class Monoblock(Computer):
    def __init__(self, computer_type,
                 trade_name,
                 manufacturer,
                 model,
                 cpu,
                 ram,
                 video,
                 disk,
                 size,
                 price,
                 in_stock):
        super().__init__(computer_type)
        self._trade_name = trade_name
        self._manufacturer = manufacturer
        self._model = model
        self._cpu = cpu
        self._ram = ram
        self._video = video
        self._disk = disk
        self._size = size
        self._price = price
        self._in_stock = in_stock

    @property
    def trade_name(self):
        return self._trade_name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def model(self):
        return self._model

    @property
    def cpu(self):
        return self._cpu

    @property
    def ram(self):
        return self._ram

    @property
    def video(self):
        return self._video

    @property
    def disk(self):
        return self._disk

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self._price

    @property
    def in_stock(self):
        return self._in_stock

    @trade_name.setter
    def trade_name(self, new_trade_name):
        self._trade_name = new_trade_name

    @manufacturer.setter
    def manufacturer(self, new_manufacturer):
        self._manufacturer = new_manufacturer

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @cpu.setter
    def cpu(self, new_cpu):
        self._cpu = new_cpu

    @ram.setter
    def ram(self, new_ram):
        self._ram = new_ram

    @video.setter
    def video(self, new_video):
        self._video = new_video

    @disk.setter
    def disk(self, new_disk):
        self._disk = new_disk

    @size.setter
    def size(self, new_size):
        self._size = new_size

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @in_stock.setter
    def in_stock(self, new_in_stock):
        self._in_stock = new_in_stock

    def __str__(self):
        return f"""{self.trade_name}:
                   Type: {self._computer_type}
                   Manufacturer: {self._manufacturer}
                   Model: {self._model}
                   Screen size: {self._size}
                   CPU: {self._cpu}
                   RAM: {self._ram}
                   Video: {self._video}
                   Disk: {self._disk}
                   Price: {self._price}
                   Available: {self._in_stock}"""
