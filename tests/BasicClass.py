from abc import ABC, abstractmethod


class BasicClass(ABC):

	@abstractmethod
	def __str__(self):
		pass
