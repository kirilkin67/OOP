class Car:
    # Конструктор класса Car
    def __init__(self, nomer, model, engine_type, engine_power: int, price: int, mileage=5, fuel_tank=0,
                 engine_volume=0, color="Синий", tank_value=40, max_speed=120, fuel_consumption=12, srSkor=60, jps={"x": 0, "y": 0}):
        self.nomer = nomer  # Номерной знак автомобиля
        self.model = model
        self.color = color  # Цвет автомобиля
        self.engine_type = engine_type  # Тип двигателя
        self.engine_power = engine_power  # Мощность двигателя
        self.engine_volume = engine_volume  # Объем двигателя
        self.fuel_tank = fuel_tank  # Остаток топлива в баке
        self.tank_value = tank_value  # Объем топливного бака
        self.fuel_consumption = fuel_consumption  # Расход топлива
        self.max_speed = max_speed  # максимальная скорость
        self.mileage = mileage  # Пробег
        self.price = price  # Стоимость нового
        self.current_price = 0  # Стоимость на данный момент
        self.srSkor = srSkor
        self.__jps = jps

    # Свойства класса: тип привода,
    # GPS координаты расположения в данный момент, ,
    #  меж сервисный интервал.
    def information(self, typeI=0):
        if typeI == 0:
            # полная информация
            return f'Тип мотора {self.engine_type} Цвет {self.color} Модель {self.model} Груз {self.gruz} Количество литров в баке  {round(self.tank_value)} ' \
                   f'Средняя скорость {self.srSkor} Навигация (х,y) {self.__jps["x"], self.__jps["y"]} Расход на 100 км {self.fuel_consumption}'
        elif typeI == 1:
            # перевозка груза
            return f'Груз {self.gruz} ' \
                   f'Средняя скорость {self.srSkor} Расход на 100 км {self.fuel_consumption}'
        elif typeI == 2:
            # перемещение в пространстве
            return f'Количество литров в баке  {round(self.tank_value)} Навигация (х,y) {self.__jps["x"], self.__jps["y"]} Расход на 100 км {self.fuel_consumption}'

    def __S(self, endX, endY):

        S = self.puty(endX, endY)
        return S / 100 * self.fuel_consumption, S

    def dovezet(self, endX, endY):
        if endX < 0 or endY < 0: return 'Не верные координаты'
        l, S = self.__S(endX, endY)
        if l <= self.tank_value:
            self.__jps['x'] = endX
            self.__jps['y'] = endY
            self.tank_value -= l
            return f' Вы проехали {round(S, 2)} км'
        else:
            return self.rasto()

    def azc(self, litr):
        if self.tank_value + litr <= self.fuel_tank:
            self.tank_value += litr
        else:
            print(f"Не поместится {litr} л, вы можете долить только {self.fuel_tank - self.tank_value}")

    def rasto(self):
        """
        На какое расстояние могу доехать
        :return: строка с информацией о расстоянии
        """
        return f'Заехать на АЗС вы можете проехать только {int(self.tank_value / self.fuel_consumption * 100)} км '

    def puty(self, endX, endY):
        # print("координаты ",(self.__jps['x'] , endX) ,(self.__jps['y'], endY) )
        return ((self.__jps['x'] - endX) ** 2 + (self.__jps['y'] - endY) ** 2) ** .5  # км

    def gruz(self, t):
        if t < self.gruz:
            return "В путь!!!"
        elif t == self.gruz:
            return " Вы взяли мах груз не превышайте скорость"
        else:
            return 'Перебор!!!'

    def zena(self, zenaLitr, endX, endY):
        return self.__S(endX, endY)[0] * zenaLitr

    def time(self, endX, endY):
        s = self.__S(endX, endY)[1]
        x = round(s / self.srSkor, 2)
        h = int(x)
        m = int((x - h) * 60)
        return f'Время в пути составит {h} час и {m} минут '


import random

if __name__ == "__main__":
    def fgf(mpv1, x, y):
        print(mpv1.information())
        print(mpv1.time(x, y), mpv1.dovezet(x, y))
        print(mpv1.information(2))


    mpv = Car("D", 650, 'салатовый', "bmv", 50, )
    mpv1 = Car(motor="B", gruz=3500, bakV=60, jps={"x": 100, "y": 0})
    fgf(mpv, 20, 1.10)
    print('******************')
    fgf(mpv1, -1.5, 1.10)
