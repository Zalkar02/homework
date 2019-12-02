# Задача №1

class Rectangle:						
	def __init__(self, lenght, widht):
		self.lenght = lenght # Длина
		self.widht = widht # Ширена

	def find_area(self): # Нахождение площади
		return self.lenght * self.widht

	def find_perimetr(self): # Нахождение периметра
		return (self.lenght + self.widht) * 2

	def draw_rectangle(self): # Рисуем прямоугольник
		for i in range(self.widht):
			print('*'* self.lenght)


rct = Rectangle(15, 8) 

print('Area: ', rct.find_area())
print('Perimetr: ', rct.find_perimetr())
rct.draw_rectangle()


# Задача №2

class Contact:
	def __init__(self, name, last_name, number):
		self.name = name
		self.last_name = last_name
		self.number = number

	def __str__(self):
		return self.name


class ContactList:
	cotacts_list = []

	def add_contact(self, contact):
		self.contacts_list.append(contact)

	def seacrh_contact(self, contact):
		for i in self.contacts_list:
			
	
		
pers = Contact('Nurs', '', '0777777')
print(pers)
