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