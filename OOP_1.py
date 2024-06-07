# Задача 3.1: Создайте класс Person, который имеет атрибуты name и age, и метод introduce, который выводит строку "Hello, my name is [name]
# and I am [age] years old.".
# Задача 3.2: Напишите класс Student, который наследуется от класса Person и добавляет атрибут student_id и метод study, который выводит строку
# "Student [name] is studying.".
# Задача 3.3: Разработайте класс Teacher, который также наследуется от класса Person, но добавляет атрибут subject и метод teach, который выводит
# строку "Teacher [name] is teaching [subject].".
# Задача 3.4: Создайте несколько объектов классов Person, Student и Teacher и вызовите их методы, чтобы продемонстрировать работу классов.
# Задача 3.5: Реализуйте в классе Person инкапсуляцию для атрибута age, чтобы он не мог быть изменен напрямую, но мог быть изменен через метод set_age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.__age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"Student {self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"Teacher {self.name} is teaching {self.subject}.")


julia = Student("Julia", 18, "S12345")
julia.introduce()
julia.study()

anton = Student("Anton", 18, "S12346")
anton.set_age(21)
anton.introduce()
anton.study()

margarita_invanovna = Teacher(name = "Margarita Ivanovna", subject = "Mathematics", age = 0)
margarita_invanovna.set_age(35)
margarita_invanovna.introduce()
margarita_invanovna.teach()
