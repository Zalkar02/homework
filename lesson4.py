#ЗАДАЧА №1

school = {
	"1a": 30,
	"1b": 26,
	"2a": 34,
	"2b": 25,
	"3a": 23,
	"3b": 20,
	"4a": 28,
	"4b": 30,
	}
i = 0
for key, value in school.items():
	print("В классе",key, value, "учеников")
school["3b"] = 25 #перезапесали значение
print("В класс 3b добавели ещё 5 учеников")
school.setdefault("1c", 23) #добавили новый элемент
print("В школе новый класс")
del school["4a"] #удаляем элемент
print("В школе расформирован класс 4a")
for key, value in school.items():
	print("В классе",key, value, "учеников")
	i += value
print('Общее количества учеников', i)
print("Задача №1 завершина")


#ЗАДАЧА №2

# Создайте словарь, где ключами являются числа, а значениями – строки. Примените к нему метод items(), 
# полученный объект dict_items передайте в написанную вами функцию, которая создает и возвращает новый 
# словарь, "обратный" исходному, т. е. ключами являются строки, а значениями – числа

nums = {
	1 : 'one',
	2 : 'two',
	3 : 'three',
	4 : 'four',
	5 : 'five'
}
nums1 = {}
#способ 1
for key, value in nums.items():
	print(key,value)
	nums1 [value] = key

for key, value in nums1.items():
	print(key,value)
print("способ 1")
#способ 2
nums2 = {value: key for key, value in nums.items()}
for key, value in nums2.items():
	print(key,value)
print("способ 2")

print("Задача №2 завершина")