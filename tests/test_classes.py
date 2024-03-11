import pytest
from src.classes import Category, Product


@pytest.fixture()
def categories():
	return Category('Kitchen', 'everything for cooking', [])


def test_init_categories(categories):
	assert categories.name == 'Kitchen'
	assert categories.description == 'everything for cooking'
	assert categories.goods == []
	assert categories.category_counter == 1
	assert categories.unique_goods_counter == 0


@pytest.fixture()
def products():
	return Product('cup', 'for tasty beverages', 10.50, 7)


def test_init_products(products):
	assert products.name == 'cup'
	assert products.description == 'for tasty beverages'
	assert products._price == 10.50
	assert products.amt_in_stock == 7


def test_get_goods_setter():
	category = Category("Electronics", "electronic devices", [])
	product1 = Product("Phone", "Smartphone", 1000, 10)
	product2 = Product("Phone2", "Stupidphone", 1500, 5)

	category.get_goods = product1
	assert len(category.goods_list) == 1
	assert category.goods_list[0] == product1

	with pytest.raises(ValueError):
		category.get_goods = Product("Android", "really smart", 0, 0)


def test_average_price():
	category = Category("Electronics", "electronic devices", [])
	product1 = Product("Phone", "Smartphone", 1000, 10)
	product2 = Product("Phone2", "Stupidphone", 1500, 5)
	category.get_goods = product1
	category.get_goods = product2

	expected_average_price = (1000 * 10 + 1500 * 5) / 15
	assert category.average_price() == expected_average_price
