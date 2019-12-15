class Todo:
	todo_items = []

	def add_todo(self, obj):
		self.todo_items.append(obj)

	def list_items(self):
		for i in self.todo_items:
			print(f'{i}: {i.is_done}')

	def find(self, word):
		for i in self.todo_items:
			if word in i.task:
				print(f'{self.todo_items.index(i)}, {i}: {i.is_done}')



class Todoitem:
	def __init__(self, task):
		self.task = task
		self.is_done = False

	def check(self):
		self.is_done = False

	def uncheck(self):
		self.is_done = True

	def __str__(self):
		return self.task


todo = Todo()

t1 = Todoitem('Сделать дз')
todo.add_todo(t1)
t2 = Todoitem('Убратся в комнате')
todo.add_todo(t2)
t3 = Todoitem('Потапить печку')
todo.add_todo(t3)

todo.list_items()
t1.uncheck()
todo.find('дз')
t2.uncheck()
todo.find('брат')
t3.uncheck()
todo.find('чку')