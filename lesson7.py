def num(a, b):
	if a >= b:
		return a
	else:
		return str(b) + ' ' + str(num(a,b-1))


def num1(n):
	if n == 1:
		return 1
	else:
		return str(num1(n-1)) + " " + str(n)

def num2(n):
	if n == 1:
		return 1
	elif n % 2 == 0:
		n -= 1
	if n % 2 != 0:
		return str(n) + ' ' + str(num2(n-2))

#Задача №1

a = int(input('Введите число а:  '))
b = int(input('Введите число b:  '))
print(num(a, b), '\n Задача №1 завершина')

#Задача №2

num = int(input('Введите число:  '))
print(num1(num), '\n Задача №2 завершина')

#Задача №3

num = int(input('Введите число:  '))
print(num2(num), '\n Задача №3 завершина')