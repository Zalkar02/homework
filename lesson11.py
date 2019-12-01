# Задача №1

class Calculator:
	def __init__(self, num1):
		self.num1 = num1

	def __add__(self, num2):
		return self.num1 + num2

	def __sub__(self, num2):
		return self.num1 - num2

	def __mul__(self, num2):
		return self.num1 * num2

	def __div__(self, num2):
		return self.num1 / num2


cl = Calculator(50)
print(cl.__add__(20*5))
print(cl.__sub__(100//4))
print(cl.__mul__(5+5))
print(cl.__div__(18-15))
print('=========================================================')


# Задача №2

class BankAccount:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.balance = 0

	def deposit(self, num):
		self.balance += num
		print('Счёт паполнен')
		print(f'{self.name} {self.surname}')
		print(f'Баланс: {self.balance}')

	def _withdraw(self, num):
		self.balance -= num
		print('Транзакция выполнена')
		print(f'{self.name} {self.surname}')
		print(f'Баланс: {self.balance}')


class MinimumBalanceAccount(BankAccount):
	"""docstring for MinimumBalanceAccount"""
	def __init__(self, name, surname):
		self.minimum_balance = 0
		super().__init__(name, surname)
	
	def withdraw(self, num):
		if self.balance-num > self.minimum_balance:
			self._withdraw(num)
		else:
			print('Не хватает средств')
			print(f'{self.name} {self.surname}')
			print(f'Баланс: {self.balance}')


per = MinimumBalanceAccount('Zalkar', 'Azis uulu')
per.deposit(int(input('Ведите сумму пополнения:  ')))
per.withdraw(int(input('Сколько хотите вывести:  ')))
per.withdraw(int(input('Сколько хотите вывести:  ')))
per.withdraw(int(input('Сколько хотите вывести:  ')))