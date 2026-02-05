class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)

class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        Product.__init__(self, product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        ElectronicProduct.__init__(self, product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print("RAM:", self.ram)
        print("Storage:", self.storage)


phone = MobilePhone("iPhone 15", 80000, "Apple", "1 Year", "8GB", "256GB")

phone.display_product()
phone.display_electronic_product()
phone.display_mobile_details()
