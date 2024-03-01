class Category:
	name: str
	description: str
	goods: list

	category_counter = 0
	unique_goods_counter = 0
	goods = []

	def __init__(self, name, description, goods):
		self.name = name
		self.description = description
		self.__goods = goods
		Category.category_counter += 1
		Category.unique_goods_counter += len(set(goods))

class Product:
	name: str
	description: str
	price: float
	amt_in_stock: int

	def __init__(self, name, description, price, amt_in_stock):
		self.name = name
		self.description = description
		self._price = price
		self.amt_in_stock = amt_in_stock