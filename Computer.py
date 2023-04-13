class Computer:
    def __init__(self, computer_type):
        self._computer_type = computer_type

    @property
    def computer_type(self):
        return self._computer_type

    @computer_type.setter
    def computer_type(self, new_computer_type):
        self._computer_type = new_computer_type
