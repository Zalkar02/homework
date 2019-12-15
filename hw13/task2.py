class Animal:
	def eat(self):
		print('eat')

	def sleep(self):
		print('sleep')

	def make_sound(self):
		print('sound')


class AnimalWithHorn:
	def gore(self):
		print('gore')


class Cow(Animal, AnimalWithHorn):
	def make_sound(self):
		print('My my')


class Ram(Animal, AnimalWithHorn):
	def make_sound(self):
		print('Me me')


cow = Cow()
cow.eat()
cow.sleep()
cow.make_sound()
cow.gore()

ram = Ram()
ram.eat()
ram.sleep()
ram.make_sound()
ram.gore()