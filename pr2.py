class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = 'женат' if self.is_married else 'не женат'
        print(f'Имя: {self.full_name}, Возраст: {self.age}, Семейное положение: {marital_status}')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_marks(self):
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Оценки: {self.marks}, Средняя оценка: {self.average_marks()}')

class Teacher(Person):
    base_salary = 3000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus = 0.05 * self.base_salary * (self.experience - 3)
        else:
            bonus = 0
        return self.base_salary + bonus

def create_students():
    student1 = Student('Байэл Муратбеков', 19, False, {'Математика': 4, 'Химия': 5, 'Английский': 5})
    student2 = Student('Алибек Кайыпбеков', 18, False, {'Математика': 4, 'Химия': 3, 'Английский': 5})
    student3 = Student('Куткелди Жапаров', 20, False, {'Математика': 5, 'Химия': 5, 'Английский': 5})
    return [student1, student2, student3]

math_teacher = Teacher('Гапаров Ринат', 35, True, 6)
math_teacher.introduce_myself()
salary = math_teacher.calculate_salary()
print(f'Зарплата учителя: {salary} сом')

students = create_students()
for student in students:
    student.introduce_myself()
    print(f'{student.average_marks():.2f}')
    print('-' * 20)