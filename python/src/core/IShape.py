from abc import ABC, abstractmethod

class IShape(ABC):
	@abstractmethod
	def square(self):
		pass

	@abstractmethod
	def length(self):
		pass

	@abstractmethod
	def shift(self, point):
		pass

	@abstractmethod
	def rot(self, phi):
		pass

	@abstractmethod
	def symAxis(self, i):
		pass

	@abstractmethod
	def cross(self, IShape):
		pass

	@abstractmethod
	def __str__(self):
		pass