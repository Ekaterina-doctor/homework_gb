# 1
from time import sleep


class TrafficLight:
    def __init__(self, color):
        self._color = color

    def running(self):
        for key, value in self._color.items():
            sleep(value)
            print(key)


traf = TrafficLight(color={"Красный": 7, "Желтый": 2,"Зеленый": 7})
traf.running()

# 2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


result = MassCount(20, 25000, 25)
print(result.mass())

# 3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
       return f'{sum(self._income.values())}'


result = Position('Alex', 'Parker', 'Lawyer', 200000, 15000)
print(result.get_full_name())
print(result.position)
print(result.get_total_income())

# 4

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Over speed of {self.name}'
        else:
            return f'Speed of {self.name} is normal'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Over speed of {self.name} '
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


jaguar = SportCar(150, 'Red', 'Jaguar', False)
volvo = TownCar(40, 'Black', 'Volvo', False)
skoda = WorkCar(80, 'White', 'Skoda', True)
audi = PoliceCar(90, 'Blue',  'Audi', True)
print(skoda.turn_left())
print(jaguar.show_speed())
print(volvo.show_speed())
print(skoda.show_speed())
print(audi.show_speed())

# 5
class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Взят {self.title}. Запуск отрисовки ручкой.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Взят {self.title}. Запуск отрисовки карандашом.'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Взят {self.title}. Запуск отрисовки маркером.'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())