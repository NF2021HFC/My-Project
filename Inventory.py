class Inventory:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    def add_product(self, product, quantity):
        for item in self._products:
            if item['product'].name == product.name:
                item['quantity'] += quantity
                print(f"{product.name} added to inventory of quantity {quantity}")
                break
        else:
            self._products.append({'product': product, 'quantity': quantity})
            print(f"Added {quantity} to {product.name}")

    def print_inventory(self):
        for item in self._products:
            print(f"Product: {item['product'].name}, Quantity: {item['quantity']}")


