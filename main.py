from Computer import Computer
from Desktop import Desktop
from MiniPC import MiniPC
from Monoblock import Monoblock
from Notebook import Notebook
from Shop import Shop


global stock
stock = Shop()


def welcome_menu():
    print("""Добро пожаловать в магазин компьютеров 'У Барсика'!
             Пожалуйста, положите на клавиатуру одну сосиску и сделайте выбор из меню
             (раскладка должна быть латинской):
             'a' - оформить поступление компьютеров на склад
             'b' - просмотреть список компьютеров в наличии
             'c' - заказать компьютер
             'q' - выйти из магазина
             """)

    user_request = str(input("Ваш выбор:  ")).lower()
    match user_request:
        case 'a':
            warehouse()
        case 'b':
            stock.print()
            welcome_menu()
        case 'c':
            order()
            welcome_menu()
        case 'q':
            print('Спасибо за визит! Заходите ещё!')
            exit()
        case 'с':
            print('Пожалуйста, проверьте раскладку клавиатуры!')
            welcome_menu()
        case _:
            print("Пожалуйста, воспользуйтесь опциями, предусмотренными меню!")
            welcome_menu()


def warehouse():
    print("""'У Барсика'. Оболочка учёта поступлений на склад.
             Пожалуйста, ведитсделайте выбор из меню
             (раскладка должна быть латинской):
             'a' - начать/продолжить ввод
             'q' - выйти из подсистемы
             """)
    menu_request = str(input("Выберите операцию:  ")).lower()
    match menu_request:
        case 'a':
            print("""Введите далее тип нового компьютера:
            'd' - настольный компьютер
            'n' - ноутбук
            'm' - мини-компьютер
            'b' - компьютер-моноблок
            """)
            computer_type = str(input("Тип нового компьютера:  ")).lower()
            match computer_type:
                case 'd':
                    new_computer_1 = Desktop(Desktop, 'Barsik Ultra',
                                           'HP', 'UltraSmart', 'Intel i100500',
                                           16, 'GF XXXL 9000 16Gb', 2, 16, 1000, True)
                    stock.warehouse_delivery(new_computer_1)
                case 'n':
                    new_computer_2 = Notebook(Notebook, 'Meow Note',
                                            'HP', 'UltraSmart', 'Intel iover9000',
                                             16, 'GF XXXL 9000 16Gb', 2, 16, 1000, True)
                    stock.warehouse_delivery(new_computer_2)
                case 'b':
                    new_computer_3 = Monoblock(Monoblock, 'Barsik Mono',
                                             'HP', 'UltraQuick', 'Intel iVeryMnogo',
                                             16, 'GF XXXL 9000 16Gb', 2, 16, 1000, True)
                    stock.warehouse_delivery(new_computer_3)
                case 'm':
                    new_computer_4 = MiniPC(MiniPC, 'Barsik Mini',
                                          'HP', 'UltraSmart', 'Intel i100500',
                                           16, 'GF XXXL 9000 16Gb', 2, 16, 1000, True)
                    stock.warehouse_delivery(new_computer_4)
                case _:
                    print("Пожалуйста, воспользуйтесь опциями, предусмотренными меню!")
                    warehouse()
        case 'q':
            welcome_menu()
        case _:
            print("Пожалуйста, воспользуйтесь опциями, предусмотренными меню!")
            warehouse()
    stock.print()
    warehouse()


def order():
    stock.print()
    ordered_pc = stock.sell_computer(computer=stock.get_computer()[0])
    print(f"Ваш заказ {ordered_pc} уже на пути к Вам! Не забудьте про рыбов для курьера!")


if __name__ == '__main__':
    welcome_menu()
