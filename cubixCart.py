

from decimal import Decimal, ROUND_HALF_UP

class Product:
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = Decimal(unit_price)

class ShoppingCart:
    def __init__(self, tax_rate=0.0):
        self.items = []
        self.tax_rate = Decimal(tax_rate) / 100
        self.total_price = Decimal(0)
        self.total_tax = Decimal(0)

    def add_item(self, product, quantity):
        for _ in range(quantity):
            self.items.append(product)
            self.total_price += product.unit_price

    def calculate_tax_and_total(self):
        self.total_tax = self.total_price * self.tax_rate
        self.total_price += self.total_tax

        # Round the totals to 2 decimal places
        self.total_price = self.total_price.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
        self.total_tax = self.total_tax.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)

# Step 1
cart1 = ShoppingCart()
dove_soap = Product("Dove Soap", 39.99)
cart1.add_item(dove_soap, 5)
cart1.calculate_tax_and_total()
print("Step 1 - Total Price:", cart1.total_price)

# Step 2
cart2 = ShoppingCart()
cart2.add_item(dove_soap, 5)
cart2.add_item(dove_soap, 3)
cart2.calculate_tax_and_total()
print("Step 2 - Total Price:", cart2.total_price)

# Step 3
cart3 = ShoppingCart(tax_rate=12.5)
axe_deo = Product("Axe Deo", 99.99)
cart3.add_item(dove_soap, 2)
cart3.add_item(axe_deo, 2)
cart3.calculate_tax_and_total()
print("Step 3 - Total Price:", cart3.total_price)
print("Step 3 - Total Tax:", cart3.total_tax)