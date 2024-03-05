from abc import ABC, abstractmethod


class BasicClass(ABC):

	@abstractmethod
	def __str__(self):
		pass

	@abstractmethod
	def make_product(self):
		pass


class MixinInfo:
	def __init__(self, *args):
		print(repr(self))

	def __repr__(self):
		# return f"{self.__class__.__name__}({', '.join(map(str, self.__dict__.values()))}"
		info = ', '.join([f"{key}={value!r}" for key, value in self.__dict__.items()])
		return f"{self.__class__.__name__}({info})"
