# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця. Для базового класу це може бути рядок із написом
# «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.
# Завдання 5
# Для класів із попереднього завдання реалізуйте магічний метод str, а також метод int (який повертає вік
# службовця).

class Employer:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
    
    @staticmethod
    def Print():
        print("This is Employer class")

    def __str__(self) -> str:
        return f'Name: {self._name}, Age: {self._age}'
    
    def __int__(self):
        return self._age
    
class President(Employer):

    @staticmethod
    def Print():
        print("This is President class")

    def __str__(self) -> str:
        return f'{super().__str__()}, Position: President'

class Worker(Employer):
    @staticmethod
    def Print():
        print("This is Worker class")

    def __str__(self) -> str:
        return f'{super().__str__()}, Position: Worker'

class Manager(Employer):
    @staticmethod
    def Print():
        print("This is Manager class")

    def __str__(self) -> str:
        return f'{super().__str__()}, Position: Manager'


president = President("Barack Obama", 80)
worker = Worker("Bobby", 32)
manager = Manager('Judas', 43)

president.Print()
print(president)
print(int(president))

manager.Print()
print(manager)
print(int(manager))

worker.Print()
print(worker)
print(int(worker))