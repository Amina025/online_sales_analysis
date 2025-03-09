from product_manager import ProductManager
from product import Product
from cart import Cart

manager = ProductManager()

# Dodavanje proizvoda
product1 = Product("Laptop", 1500, 5)
product2 = Product("Telefon", 800, 10)
product3 = Product("Televizor", 1000, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

cart = Cart()
cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

cart.display_cart()
print(f"Ukupna vrijednost korpe: {cart.calculate_total()} KM")

# Prikaz proizvoda i ukupne vrijednosti
manager.display_products()
print(f"Ukupna vrijednost inventara: {manager.total_inventory_value()} KM")