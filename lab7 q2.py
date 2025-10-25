# q2) An onlien store has a baseclass product and two derived classes a) electronics and b) clothing

# electrionic: brand and warranty (attributes)
# clothing : size and fabric type (attributes)



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ₹{self.price}")


class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        
        super().display()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty} years")


class Clothing(Product):
    def __init__(self, name, price, size, fabric_type):
        
        super().__init__(name, price)
        self.size = size
        self.fabric_type = fabric_type

    def display(self):
        
        super().display()
        print(f"Size: {self.size}")
        print(f"Fabric Type: {self.fabric_type}")


electronic_item = Electronics("phone", 25000, "Samsung", 2)
clothing_item = Clothing("T-Shirt", 799, "L", "Cotton")

electronic_item.display()
clothing_item.display()
