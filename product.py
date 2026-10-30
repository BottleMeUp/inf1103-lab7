from abc import ABC, abstractmethod 

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        print("Update Stock")
        if quantity < 0:
            print("Stock cannot be negative.")
            return
    
        self.__stock = quantity
        print(f"\nNew Stock Quantity: {self.__stock}")
        print("\nStock updated successfully! ")

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def get_stock(self):
        return self.__stock

    @abstractmethod
    def get_fulfilment_info(self):
        pass

class CanBeShipped(ABC)
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)

        self.__weight = weight

    # Override the parent method
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}")

    def get_fulfilment_info(self):
        print("Product requires physical shipping")

    def calculate_shipping_cost(self):
        shipping_cost = self.__weight * 100
        return shipping_cost

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)

        self.__download_size = download_size

    # Override the parent method
    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size}")

    def get_fulfilment_info(self):
        print("Product is delivered digitally")
    

            







    