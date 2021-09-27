class Persona:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.age = None
        self.job = None
        self.pol = None
        self.docs = None
        self.place_w = None
        self.car = None
        self.cash = None
        self.prava = None
        self.otpusk = None
        self.work_time = None

    def work(self, place_work: str, how_much_do_you_work: int):
        self.place_w = place_work
        self.work_time = how_much_do_you_work
        if self.age >= 18:
            self.job = 'you can working'
        self.__otpusk()

    def set_age(self, age: int):
        self.age = age
        self.__get_passport()
        self.__get_prava_in_car()

    def set_sex(self, sex: str):
        self.pol = sex

    def money(self, you_cash: int):
        """ cash in dollars """
        self.cash = you_cash
        self.__machine()

    def __machine(self):
        """ Для работы этой функции нужна money """
        if self.cash >= 5000:
            self.car = 'you can buy car'

    def __get_prava_in_car(self):
        """ Для работы этой функции нужна "set_age" """
        if self.age >= 18:
            self.prava = 'you can get prava in car'

    def __get_passport(self):
        """ Для работы этой функции нужно вызвать функцию "set_age" """
        if self.age >= 14:
            self.docs = 'you can get passport'
        else:
            self.docs = "you can't get passport"

    def __otpusk(self):
        if self.place_w and self.work_time > 100:
            self.otpusk = 'you can drive in otpusk'

    def set_passport(self, kem_vydan: str, kogda_vydan: str, number_passport: str):
        if self.age and self.age >= 14:
            self.docs = f'passport vydan: {kem_vydan}, data vydachi: {kogda_vydan}, number: {number_passport}'
