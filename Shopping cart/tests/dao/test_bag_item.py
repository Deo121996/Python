from dao.bag_item import BagItem
from dao.product import Product

#test data
product = Product(price=100)
bag_item = BagItem(product)

#test cases
def test_increase_quantity():
    bag_item.increase_quantity(1)
    assert bag_item.get_product_quantity() == 1

def test_decrease_quantity():
    bag_item.increase_quantity(3)
    bag_item.decrease_quantity(1)
    assert bag_item.get_product_quantity() == 3

def test_get_bag_item_total():
    assert bag_item.get_bag_item_total() == 337.5

def test_get_product_quantity():
    bag_item.decrease_quantity(1)
    assert bag_item.get_product_quantity() == 2
