i = 1

# ЗАДАЧА №1

password = 'qwerty123'
input_pass = input("Ведите пороль:  ")
input_pass = input_pass.lower().strip()

if password == input_pass:
	print('Пороь верен. Добро пожалывать)')
else:
	print('Извените пороль не подошол, попробуйте ещё раз')

#ЗАДАЧА №2



while i:
	temperature = int(input('Ведите температуру:  '))  
	if temperature == -30:
		print('Там так холодно, лучше дома сиди!')
		i = 0
	elif -30 < temperature <= 0:
		print('Холодновато. Оденься потеплее!')
		i = 0
	elif 0 < temperature <= 15:
		print('Прохладно. Куртку накинь!')
		i = 0
	elif 15 < temperature <= 30:
		print('Тепло. Иди погуляй в парке!')
		i = 0
	elif 30 < temperature < 50:
		print('Ого, как жарко!')
		i = 0
	elif temperature == 50:
		print('Там такая жара, лучше сиди дома!')
		i = 0
	else:
		print('Ошибка! попробуйте ещё раз')

#ЗАДАЧА №3

i = 1
men = ''
weight = ''

while i:
	men = input("Вы парень или девушка? ")
	men = men.lower().strip()
	if men == 'парень':
		weight = int(input('Cколько был вес гантел которыми ты занимался? '))
		if 0 < weight < 10:
			print('Ммм, мог бы и полутше')
		elif 10 <= weight <= 40:
			print('Молодец 5 тебе')
		elif weight > 40:
			print('Что ты врёш?')
		else:
			print('Почему нечего не сделал?')
		i = 0
	elif men == 'девушка':
		weight = int(input('Cколько был вес гантел которыми ты занималась? '))
		if 0 < weight < 5:
			print('Ммм, могла бы и полутше')
		elif 10 <= weight <= 30:
			print('Молодец 5 тебе')
		elif weight > 30:
			print('Что ты врёш?')
		else:
			print('Почему нечего не сделала?')
		i = 0
	else:
		print('Ошибка! попробуйте ещё раз')
