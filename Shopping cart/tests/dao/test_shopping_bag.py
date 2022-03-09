from dao.shopping_bag import ShoppingBag
from dao.product import Product

bag = ShoppingBag()

product1 = Product(price=39.99, product_id="Dove", name="Dove", weight="90g")
product2 = Product(price=99.99, product_id="Axe", name="Axe", weight="100g")
bag.add_product(product=product1, qty=2)
bag.add_product(product=product2, qty=2)

def test_get_bag_details():
    """
    Test Case for get_bag_details
    """
    result = bag.get_bag_details()
    del result["bag_id"]
    assert result == {
        "products": [
            {
                "itemId": "Dove",
                "category": "default",
                "bagItemTotal": 89.98,
                "quantity": 2,
                "salesTaxRate": 12.5,
                "productDetails": {"name": "Dove", "weight": "90g"},
            },
            {
                "itemId": "Axe",
                "category": "default",
                "bagItemTotal": 224.98,
                "quantity": 2,
                "salesTaxRate": 12.5,
                "productDetails": {"name": "Axe", "weight": "100g"},
            }
        ],
        "total": 314.96,
    }

def test_get_bag_details_with_category_luxury_items():
    """
    Test Case for get_bag_details - Test salesTaxRate varries according to product category
    """
    luxury_product = Product(price=1000.05, category="luxury_items", product_id="l1", name="Antique Sword", weight="2kg")
    bag.add_product(product=luxury_product, qty=1)
    result = bag.get_bag_details()
    bag.remove_product_quantity(luxury_product.product_id)
    del result["bag_id"]
    assert result == {
        "products": [
            {
                "itemId": "Dove",
                "category": "default",
                "bagItemTotal": 89.98,
                "quantity": 2,
                "salesTaxRate": 12.5,
                "productDetails": {"name": "Dove", "weight": "90g"},
            },
            {
                "itemId": "Axe",
                "category": "default",
                "bagItemTotal": 224.98,
                "quantity": 2,
                "salesTaxRate": 12.5,
                "productDetails": {"name": "Axe", "weight": "100g"},
            },
            {
                "itemId": "l1",
                "productDetails": {"name": "Antique Sword", "weight": "2kg"},
                "category": "luxury_items",
                "salesTaxRate": 28,
                "quantity": 1,
                "bagItemTotal": 1280.07,
            }
        ],
        "total": 1595.02,
    }

def test_add_product():
    """
    Test Case for add_product
    """
    bag.remove_product_quantity(product2.product_id, 1)
    bag.add_product(product=product2, qty=1)
    assert len(bag.get_all_bag_items()) == 2

def test_remove_product_quantity():
    """
    Test Case for remove_product_quantity - decrease quantity of the product
    """
    bag.remove_product_quantity(product1.product_id, 2)
    result = bag.get_bag_details()
    assert result["total"] == 224.98

def test_remove_product_quantity_remove_product():
    """
    Test Case for remove_product_quantity - remove entire product from bag
    """
    bag.remove_product_quantity(product2.product_id)
    result = bag.get_bag_details()
    assert result["total"] == 0

def test_get_all_bag_items():
    """
    Test Case for get_all_bag_items
    """
    bag.add_product(product=product2, qty=1)
    result = bag.get_all_bag_items()
    assert result == [
        {
            "itemId": "Axe",
            "productDetails": {"name": "Axe", "weight": "100g"},
            "category": "default",
            "salesTaxRate": 12.5,
            "quantity": 1,
            "bagItemTotal": 112.49,
        }
    ]
