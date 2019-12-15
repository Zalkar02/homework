from abc import ABC, abstractmethod

class Computer(ABC):
	@abstractmethod
	def connect_to_projector(self):
		pass


class Loptop(Computer):
	def connect_to_projector(self):
		print('connect to projector')


class Desktop(Computer):
	def connect_to_projector(self):
		print('connect to projector')


class Projector:
	def connect(self, obj):
		if isinstance(obj, Loptop):
			obj.connect_to_projector()
		else:
			print('error 404')


l = Loptop()
d = Desktop()
p = Projector()

p.connect(l)
p.connect(d)