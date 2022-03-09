
from dao.bag_item import BagItem
from dao.product import Product
from utils.helper import get_random_uuid, get_rounded_value
from utils.constants import BAG_ID_LENGTH

class ShoppingBag:
    """
    ShoppingBag class
    """
    def __init__(self):
        self.bag_id = get_random_uuid(BAG_ID_LENGTH)
        self.bag_items = dict()
    
    def add_product(self, product: Product, qty):
        """
        Add product to the shopping bag
        """
        bag_item = self.bag_items.get(product.product_id)
        if not bag_item:
            bag_item = BagItem(product)
            self.bag_items[bag_item.product_id] = bag_item

        bag_item.increase_quantity(qty)
        return True

    def remove_product_quantity(self, product_id, qty=0):
        """
        Remove product or decrease quanity of the product
        :param product_id:
        :param qty - if qty - 0, remove product from the bag. if qty - non-zero, decrease qty of the product:
        """
        bag_item = self.bag_items.get(product_id)
        if not bag_item:
            print("No product available with id %s", product_id)
            return False
        bag_item.decrease_quantity(qty)

        if not qty or not bag_item.get_product_quantity():
            del self.bag_items[product_id]
        return True

    def get_bag_details(self):
        """
        Get details for the bag such as product list, total cost
        :return result:
        """
        total = 0
        for _, item in self.bag_items.items():
            total += item.get_bag_item_total()
        result = dict()
        result["products"] = self.get_all_bag_items()
        result["bag_id"] = self.bag_id
        result["total"] = get_rounded_value(total)
        return result

    def get_all_bag_items(self):
        """
        get all bag items for the shopping bag
        :return bag_items:
        """
        bag_items = list()
        for item in self.bag_items.values():
            bag_items.append(item.get_bag_item_details())
        return bag_items
