from utils.string_utils import get_random_uuid
from utils.constants import PRODUCT_ID_LENGTH
class Product:
    """
    Product class
    """
    def __init__(self, price=None, product_id=None, **product_details):
        self.product_id = get_random_uuid(PRODUCT_ID_LENGTH) if not product_id else product_id
        self.price = price
        #Field to store product details like colour, size, length etc.
        self.product_details=dict(product_details)
