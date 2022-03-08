from dao.product import Product


class BagItem(Product):
    """
    BagItem class inherits Product
    """
    def __init__(self, product: Product, qty=0):
        Product.__init__(self, product_id=product.product_id, price=product.price)
        self.qty = qty

    def get_bag_item_total(self):
        """
        Get total for bag item
        """
        return self.price * self.qty
    
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
