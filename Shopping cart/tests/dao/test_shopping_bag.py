from dao.shopping_bag import ShoppingBag
from dao.product import Product

bag = ShoppingBag()
product1 = Product(price=100, product_id="p1")
product2 = Product(price=50, product_id="p2")
product3 = Product(price=500, product_id="p3")
bag.add_product(product=product1, qty=5)
bag.add_product(product=product2, qty=2)

def test_add_product():
    bag.add_product(product=product3, qty=1)
    assert len(bag.get_bag_items()) == 3

def test_remove_product_quantity():
    bag.remove_product_quantity(product1.product_id, 2)
    result = bag.get_bag_details()
    assert result["total"] == 900


def test_get_bag_details():
    result = bag.get_bag_details()
    del result["bag_id"]
    assert result == {
        "products": [
            {"item_id": "p1", "bagItemTotal": 300, "quantity": 3},
            {"item_id": "p2", "bagItemTotal": 100, "quantity": 2},
            {"item_id": "p3", "bagItemTotal": 500, "quantity": 1},
        ],
        "total": 900,
    }

def test_get_bag_items():
    result = bag.get_bag_items()
    print(result)
    assert result == [
    {"item_id": "p1", "bagItemTotal": 300, "quantity": 3},
    {"item_id": "p2", "bagItemTotal": 100, "quantity": 2},
    {"item_id": "p3", "bagItemTotal": 500, "quantity": 1},
]
