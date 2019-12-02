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
	contacts_list = []

	def add_contact(self, contact): # Добовляем в список
		self.contacts_list.append(contact)

	def seacrh_contact(self, contact): # Ищем контакт
		for i in self.contacts_list:
			if i == contact:
				print(f'Name: {i.name} \nLast name: {i.last_name} \nNumber: {i.number}')

	def remove_contact(self, contact): # Удаляем контакт
		for i in self.contacts_list:
			if i == contact:
				self.contacts_list.remove(contact)
				print('Сontact deleted')
				print('____________________________')		

	def all_contacts(self): # Показываем весь список
		for i in self.contacts_list:
			print(f'Name: {i.name} \nLast name: {i.last_name} \nNumber: {i.number}')
			print('____________________________')		
		
cnt1 = Contact('Nurs', '', '0777777')
cnt2 = Contact('Zalkar', '', '0705 42 01 72')
cnt3 = Contact('Tolubai', '', '07075644565')
cnt4 = Contact('Chyngyz', '', '05054654847')
cnt5 = Contact('Stela', '', '055457564/98')

cnlist = ContactList()
cnlist.all_contacts()
cnlist.add_contact(cnt1)
cnlist.add_contact(cnt2)
cnlist.add_contact(cnt3)
cnlist.add_contact(cnt4)
cnlist.add_contact(cnt5)
cnlist.seacrh_contact(cnt1)
print('''

	''')
cnlist.all_contacts()
cnlist.remove_contact(cnt5)
cnlist.remove_contact(cnt4)
cnlist.all_contacts()