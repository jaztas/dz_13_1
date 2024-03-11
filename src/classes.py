from src.BasicClass import BasicClass, MixinInfo


class Category(MixinInfo):
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
		super().__init__()
		Category.category_counter += 1
		Category.unique_goods_counter += len(set(goods))

	def __len__(self):
		result = 0
		for i in self.__goods:
			result += i.amt_in_stock
		return result

	def __str__(self):
		return f'{self.name}, количество продуктов: {len(self)} шт.'

	@property
	def get_goods(self):
		result = ''
		for prod in self.__goods:
			result += f"{prod.name}, {prod.price} руб. Остаток: {prod.amt_in_stock} шт."
		return print(result)

	@get_goods.setter
	def get_goods(self, product):
		# if isinstance(product, Product):
		# 	self.__goods.append(product)
		if product.amt_in_stock == 0:
			raise ValueError('Товар с нулевым количеством не может быть добавлен!')
		if isinstance(product, Product):
			self.__goods.append(product)

	@property
	def goods_list(self):
		return self.__goods


class Product(BasicClass, MixinInfo):
	name: str
	description: str
	price: float
	amt_in_stock: int

	def __init__(self, name, description, price, amt_in_stock):
		self.name = name
		self.description = description
		self._price = price
		self.amt_in_stock = amt_in_stock
		super().__init__()

	def __str__(self):
		return f'{self.name}, {self._price} руб. Остаток: {self.amt_in_stock} шт.'

	def __add__(self, other):
		# if isinstance(other, self.__class__):
		if type(self) == type(other):
			result = (self._price * self.amt_in_stock) + (other._price * other.amt_in_stock)
			return result
		raise TypeError('Складывать можно только объекты одного класса!')

	@classmethod
	def make_product(cls, name, description, price, amt_in_stock, goods):
		for i in goods:
			if name == i.name:
				amt_in_stock += i.amt_in_stock
				if price < i.price:
					price = i.price
		return cls(name, description, price, amt_in_stock)

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, value):
		if value <= 0:
			print("Цена введена некорректно!")
		else:
			self._price = value


class Smartphone(Product):
	def __init__(self, name, description, price, amt_in_stock, productivity, model, memory, color):
		super().__init__(name, description, price, amt_in_stock)
		self.productivity = productivity
		self.model = model
		self.memory = memory
		self.color = color


class LawnGrass(Product):
	def __init__(self, name, description, price, amt_in_stock, made_in, growth_time, color):
		super().__init__(name, description, price, amt_in_stock)
		self.made_in = made_in
		self.growth_time = growth_time
		self.color = color


prod = Product('Продукт1', 'Классный продукт', 1000, 10)
print(prod)
smartphone = Smartphone('Superphone', 'Очень крутой', 1500, 5, '48 часов на одном заряде', '5X Pro', '128 Gb', 'Black')
print(smartphone)
lawn_grass = LawnGrass('Газон', 'Описание газона', 100, 10, 'Russland', '1 month', 'Green')
print(lawn_grass)

