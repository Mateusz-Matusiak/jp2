import json
class Product:
    def __init__(self, id: int, product_name: str, quantity: int, product_details: str):
        self.id = id
        self.product_name = product_name
        self.quantity = quantity
        self.product_details = product_details

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

class Products:
    def __init__(self, products):
        self.products = products

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)