

class Kettle:
    def turn_on(self): #Public
        print('Нажали кнопку')
        self.__boil()
        self.__check_temperature()
        self.__beep()
        self._turn_off()

    def __boil(self):
        print('Разогревание воды')

    def __check_temperature(self):
        print('Проверяем температуру воды')

    def __beep(self): #Private
        print('Звук')

    def _turn_off(self): #Protected
        print('Отключение')


my_kettle = Kettle()
my_kettle.turn_on()
my_kettle._turn_off()
my_kettle._Kettle__beep()
