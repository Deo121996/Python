
from dao.shopping_bag import ShoppingBag
from dao.product import Product

bag1 = ShoppingBag()
product1 = Product(100)
product2 = Product(50)
product3 = Product(20)

bag1.add_product(product1, 1)
bag1.add_product(product2, 1)
bag1.add_product(product3, 1)

bag1.add_product(product1, 2)
bag1.remove_product_quantity(product3.product_id, 1)
bag1.remove_product_quantity(product2.product_id, 1)
bag1.remove_product_quantity(product1.product_id, 1)
print(bag1.get_bag_details())
