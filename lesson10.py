# Задача №1

class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age


class Teacher(SchoolMember):
	salary = 0


	def tell(self, salary):
		self.salary += salary
		print(f'Имя: {self.name}')
		print(f'Возраст: {self.age}')
		return self.salary


class Student(SchoolMember):
	marks = 0


	def tell(self, mark):
		self.marks += mark
		print(f'Имя: {self.name}')
		print(f'Возраст: {self.age}')
		return self.marks


teacher = Teacher(
	name= input('Имя:  '),
	age= int(input('Возраст:  '))
	)
teacher.tell(int(input('Ведите сумму зарплаты:  ')))
teacher.tell(int(input('Ведите сумму зарплаты:  ')))
print(f'Общая сумма зарплаты: {teacher.salary}')
print('=============================================')

st = Student(
	name= input('Имя:  '),
	age= int(input('Возраст:  '))
	)
st.tell(int(input('Ведите оценку:  ')))
st.tell(int(input('Ведите оценку:  ')))
st.tell(int(input('Ведите оценку:  ')))
print(f'Всего баллов {st.marks}')
print('=============================================')


# Задача №2

class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0
		self.fuel = 70

	
	def __ad_distance(self, km):
		self.odometer += km
		print(f'odometer {self.odometer} km')


	def __subtract_fuel(self, km):
		fuel = km // 10
		if fuel <= self.fuel:
			self.__ad_distance(km)
			self.fuel -= fuel
			print('Let’s drive!')
			print(f'Fuel {self.fuel} l')
		else:
			print('Need more fuel, please, fill more!')


	def drive(self, km):
		self.__subtract_fuel(km)



cr1 = Car('Mers', 'S', 2019)
# cr1._Car__subtract_fuel(500)
cr1.drive(int(input('Ведите км:  ')))
cr1.drive(int(input('Ведите км:  ')))