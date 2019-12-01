# Задача №1

# способ 1
f = open('kyrgyzstan.txt', 'w')
f.write("""Kyrgyzstan, country of Central Asia. It is bounded by Kazakhstan on the northwest and north,
by China on the east and south, and by Tajikistan and Uzbekistan on the south and west. 
Most of Kyrgyzstan’s borders run along mountain crests. The capital is Bishkek (known from 1862 to 1926 as Pishpek and from 1926 to 1991 as Frunze).""")
f.close()

f = open('kyrgyzstan.txt')
print('Количество символов' ,len(f.read()), '\nСпособ 1 завершон')
f.close()

# способ 2
with open('kyrgyzstan.txt', 'w') as f1:
	f1.write("""Kyrgyzstan, country of Central Asia. It is bounded by Kazakhstan on the northwest and north,
by China on the east and south, and by Tajikistan and Uzbekistan on the south and west. 
Most of Kyrgyzstan’s borders run along mountain crests. The capital is Bishkek (known from 1862 to 1926 as Pishpek and from 1926 to 1991 as Frunze).""")

with open('kyrgyzstan.txt',) as f1:
	print('Количество символов' ,len(f1.read()), '\nСпособ 2 завершон', '\nЗадаяа №1 завершена')

# Задача №2

# Написать программу, которая откроет созданный в задаче 1 файл kyrgyzstan.txt, скопирует весь текст и 
# запишет его в новый файл wikipedia.txt . После этого необходимо в новый файл добавить следующий текст:
# The Kyrgyz, a Muslim Turkic people, constitute more than half the population. The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991.
# При этом не удаляйте имеющийся текст в файле wikipedia.txt . После этого выведите на экран весь текст данного файла. Задачу решить 2 способами (с with и без with).

# способ 1
f2 = open('kyrgyzstan.txt')
lines = f2.readlines()
f2.close()

f2 = open('wikipedia.txt', 'w')
for line in lines:
	f2.write(line)
f2.close()

f2 = open('wikipedia.txt', 'a')
f2.write('''The Kyrgyz, a Muslim Turkic people, constitute more than half the population. 
The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. 
Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. 
Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991. ''')
f2.close()

f2 = open('wikipedia.txt')
print(f2.read(), '\nСпособ 1 завершон')
f2.close()

# способ 1
with open('kyrgyzstan.txt') as f3:
	lines = f3.readlines()

with open('wikipedia.txt', 'w') as f3:
	for line in lines:
		f3.write(line)

with open('wikipedia.txt', 'a') as f3:
	f3.write( '''The Kyrgyz, a Muslim Turkic people, constitute more than half the population. 
The history of the Kyrgyz in what is now Kyrgyzstan dates at least to the 17th century. 
Kyrgyzstan, known under Russian and Soviet rule as Kirgiziya, was conquered by tsarist Russian forces in the 19th century. 
Formerly a constituent (union) republic of the U.S.S.R., Kyrgyzstan declared its independence on August 31, 1991. ''' )

with open('wikipedia.txt') as f3:
	print(f3.read(), '\nСпособ 2 завершон', '\nЗадаяа №2 завершена')