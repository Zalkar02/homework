# Задача №1

class Car:
	def __init__(self, make, model, year):
		self.owner = False
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0
		self.is_going = False


	def go(self, km):
		self.is_going = True
		self.odometer += km
		print(f'is going {self.is_going}')
		print(f'Одометр {self.odometer}')	


	def stop(self):
		self.is_going = False
		print(f'is going {self.is_going}')	

	
	def buy(self):
		i = input('Вы купити машину? (y/n):  ')
		if i == 'y' or i == 'д':
			self.owner = True
		print(self.make, self.model, self.year)
		print(f'Одометр {self.odometer}')
		print(f'Onwer {self.owner}')


car1 = Car(
	make= input('Mарка:  '),
	model= input('Модель:  '),
	year= input('Год:  ')
)

car1.go(int(input('Cколько проехали:  ')))
car1.stop()
car1.buy()
print('Задача №1 зовершина')


# Задача №2

class Airplane:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.max_speed
		self.odometer
		self.is_flying
	