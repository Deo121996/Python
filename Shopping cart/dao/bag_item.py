from dao.product import Product
from utils.constants import TAX_MAP
from utils.helper import get_rounded_value

class BagItem(Product):
    """
    BagItem class inherits Product
    """
    def __init__(self, product: Product, qty=0):
        Product.__init__(self, product_id=product.product_id, price=product.price, category=product.category, **product.product_details)
        self.qty = qty

    def get_tax_rate(self):
        return TAX_MAP.get(self.category or "default")


    def get_bag_item_total(self):
        """
        Get total for bag item
        """
        tax_rate = self.get_tax_rate()
        item_total = self.price * self.qty
        item_tax = item_total * tax_rate/100
        return item_total + item_tax
    
    def increase_quantity(self, qty: int):
        """
        Increase quantity of bag item
        :param qty - Quantity to increase:
        """
        if not qty:
            qty = 1
        self.qty += qty
        return True
    
    def decrease_quantity(self, qty: int):
        """
        Decrease quantity of bag item
        :param qty - Quantity to decrease:
        """
        if not qty:
            qty = 1
        self.qty -= qty
        return True

    def get_product_quantity(self):
        """
        Get quantity of the bag item
        """
        return self.qty

    def get_bag_item_details(self):
        bag_item = dict()
        bag_item["itemId"] = self.product_id
        bag_item["productDetails"] = self.product_details
        bag_item["category"] = self.category or "default"
        bag_item["salesTaxRate"] =  self.get_tax_rate()
        bag_item["quantity"] = self.qty
        bag_item["bagItemTotal"] = get_rounded_value(self.get_bag_item_total())
        return bag_item
