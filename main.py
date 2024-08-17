class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 9:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


try:
  first = Car('Ford', 100, 'f123dj.BY')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Toyota Land Cruiser', 3009471, 'A001AA.23')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Tesla Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

