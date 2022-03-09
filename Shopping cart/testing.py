
from dao.shopping_bag import ShoppingBag
from dao.product import Product

bag1 = ShoppingBag()
product1 = Product(price=39.99, category="soaps", name="Dove", weight="90g")
product2 = Product(price=99.99, category="luxury_items", name="Axe", weight="100g")
product3 = Product(20)


bag1.add_product(product1, 2)
bag1.add_product(product2, 2)
bag1.add_product(product2, 1)
bag1.add_product(product3, 1)

bag1.add_product(product1, 2)
bag1.remove_product_quantity(product3.product_id, 1)
bag1.remove_product_quantity(product2.product_id, 1)
bag1.remove_product_quantity(product1.product_id, 1)
print(bag1.get_bag_details())
