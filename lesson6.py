#ЗАДАЧА №1

def is_prime(i):
	if i <= 1000 and i % 2 > 0:
		return True
	else:
		return False

print(is_prime(int(input("Ведите число:  "))), "\nЗАДАЧА №1 завершина")

#ЗАДАЧА №2

def season(i):
	if i < 3 or i == 12:
		return 'Щас зима'
	elif 2 < i < 6:
		return 'Щас весна'
	elif 5 < i < 9:
		return 'Щас лето'
	elif 8 < i < 12:
		return 'Щас осень'
	else:
		return 'Ошибка'

print(season(int(input('Ведите число месяца от 1 до 12:  '))), "\nЗАДАЧА №2 завершина")

#ЗАДАЧА №3 

def is_year_leap(y):
	if y % 4 == 0 or (y % 100 != 0 and y % 400 == 0):
		return True
	else:
		return False

print(is_year_leap(int(input('Ведите год:  '))), "\nЗАДАЧА №3 завершина")

#ЗАДАЧА №4

def arithmetic(x, y, z):
	if z == '+':
		return int(x) + int(y)
	elif z == '-':
		return int(x) - int(y)
	elif z == '*':
		return int(x) * int(y)
	elif z == '/':
		return int(x) / int(y)
	else:
		return 'Неизвестная операция'

print(arithmetic(input('Ведите число 1 :'), input('Ведите число 2 :'), input('Ведите +, -, *, / :  ').strip()), "\nЗАДАЧА №4 завершина")

#ЗАДАЧА №5

def square(i):
	p = i * 4
	s = i * i
	d = (2*i**2)**.5
	return p, s, d
def pr_square(p, s, d):
    print(f'Периметр квадрата {p}')
    print(f'Площадь квадрата {s}')
    print(f'Диагональ квадрата {d}')

a = int(input('Ведите сторону квадрата:  '))
b = square(a)
p = b[0]
s = b[1]
d = b[2]

pr_square(p, s, d)

print("ЗАДАЧА №5 завершина")