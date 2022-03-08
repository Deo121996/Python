
from dao.bag_item import BagItem
from dao.product import Product
from utils.string_utils import get_random_uuid
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
        :param qty - qty should be 0 to remove product from shopping bag:
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
            total+= item.get_bag_item_total()
        result = dict()
        result["products"] = self.get_bag_items()
        result["bag_id"] = self.bag_id
        result["total"] = total
        return result

    def get_bag_items(self):
        """
        get all bag items for the shopping bag
        :return bag_items:
        """
        bag_items = list()
        for item in self.bag_items.values():
            bag_item = dict()
            bag_item["item_id"] = item.product_id
            bag_item["bagItemTotal"] = item.get_bag_item_total()
            bag_item["quantity"] = item.qty
            bag_items.append(bag_item)
        return bag_items
