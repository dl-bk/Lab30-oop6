# Створіть базовий клас «Домашня тварина» та похідні
# класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
# конструктора встановіть ім’я кожної тварини та її характеристики. Реалізуйте для кожного із класів наступні
# методи:
# ■ Sound — видає звук тварини (пишемо текстом в консоль);
# ■ Show — відображає ім’я тварини;
# ■ Type — відображає підвид тварини.


class Pet:
    def __init__(self, animal_type, name, age,) -> None:
        self.animaltype = animal_type 
        self.name = name
        self.age = age
    
    def sound(self):
        pass

    def show(self):
        pass
    
    def show_animal_type(self):
        pass

class Dog(Pet):
    
    def sound(self):
        print(f"{self.animaltype} {self.name} say Woof")
    
    def show(self):
        print(f"{self.name}")

    def show_animal_type(self):
        print(f"{self.animaltype}")

class Cat(Pet):

    def sound(self):
        print(f"{self.animaltype} {self.name} say Meow")

    def show(self):
        print(f"{self.name}")
    
    def show_animal_type(self):
        print(f"{self.animaltype}")

class Parrot(Pet):

    def sound(self):
        print(f"{self.animaltype} {self.name} say Chirp")

    def show(self):
        print(f"{self.name}")
    
    def show_animal_type(self):
        print(f"{self.animaltype}")

class Hamster(Pet):

    def sound(self):
        print(f"{self.animaltype} {self.name} say Peek")
    
    def show(self):
        print(f"{self.name}")
    
    def show_animal_type(self):
        print(f"{self.animaltype}")

dog = Dog('Dog', 'doggy', 3)
cat = Cat('Cat', 'kitty', 5)
parrot = Parrot('Parrot', 'kesha', 1)
hamster = Hamster('Hamster', 'stepan', 1)

dog.sound()
dog.show()
dog.show_animal_type()

cat.sound()
cat.show()
cat.show_animal_type()

parrot.sound()
parrot.show()
parrot.show_animal_type()

hamster.sound()
hamster.show()
hamster.show_animal_type()