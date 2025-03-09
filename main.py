from product_manager import ProductManager
from product import Product

manager = ProductManager()

# Dodavanje proizvoda
product1 = Product("Laptop", 1500, 5)
product2 = Product("Telefon", 800, 9)
product3 = Product("Televizor", 1000, 3)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)