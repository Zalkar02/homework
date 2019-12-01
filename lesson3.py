#	ЗАДАЧА №1

i = 0

while i < 57:
	i += 1
	print('I LOVE PYTHON '+ str(i))

print('ЗАДАЧА №1 завершина')

#	ЗАДАЧА №2

i = 0

while True:
	i += 1
	print('I LOVE PYTHON '+ str(i))
	if i == 57:
		break

print('ЗАДАЧА №2 завершина')

#	ЗАДАЧА №3

for x in range(58):
	print('I LOVE PYTHON '+ str(x))

print('ЗАДАЧА №3 завершина')

# ЗАДАЧА №4

i = 0

while i <= 534:
	i += 1
	if i % 2 == 0:
		continue
	print(i)

print('ЗАДАЧА №4 завершина')

# ЗАДАЧА №5

for i in range(23, 88, 8):
	print(i)

print('ЗАДАЧА №5 завершина')

# ЗАДАЧА №6

books = ['harry potter', 'sherlock holmes', 'idiot', 'illiada', 'never giveup']

for x in books:
	if x != 'idiot':
		print(x)

print('ЗАДАЧА №6 завершина')

# ЗАДАЧА №7

people = ['Regina', 'Erkayim', 'Begayim']
country = ['Germany', 'France', 'Spain', 'Portugal', 'Holland', 'Japan', 'South Korea','Singapore']

for x in people:	
	for y in country:
		print(f'{x} lives in {y}')

print('ЗАДАЧА №7 завершина')

# ЗАДАЧА №8

password_list = ['password', '12 3456', '12345678', 'qwerty', 'abc123','monkey', '1234567']

while True:
	password = input("Password:  ")

	if password not in password_list:
		continue
	print("password is suitable")
	break

print('ЗАДАЧА №8 завершина')