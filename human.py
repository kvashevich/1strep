class Persona:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.age = None
        self.job = None
        self.pol = None
        self.docs = None

    def __work(self):
        if self.age >= 18:
            self.job = 'you can working'

    def set_age(self, age: int):
        self.age = age
        self.__work()
        self.__get_passport()

    def set_sex(self, sex: str):
        self.pol = sex

    def __get_passport(self):
        '''
        Для работы этой функции нужно вызвать функцию "set_age"
        '''
        if self.age >= 14:
            self.docs = 'you can get passport'
        else:
            self.docs = "you can't get passport"

    def set_passport(self, kem_vydan: str, kogda_vydan: str, number_passport: str):
        if self.age and self.age >= 14:
            self.docs = f'passport vydan: {kem_vydan}, data vydachi: {kogda_vydan}, number: {number_passport}'


human = Persona('Max', 'Barskih')
human.set_age(20)
human.set_passport('nikem', 'vchera', '12031040')
print(human.docs)





