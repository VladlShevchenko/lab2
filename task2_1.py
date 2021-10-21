class Product:
    """Product class with getters and setters"""
    def __init__(self, name, price, description) :
        self.name = name
        self.price = price
        self.description = description

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):

        if not isinstance(value, str):
            raise TypeError("Product name must be a string")

        if len(value) <= 1:
            raise ValueError("Product name must contain at least 2 characters")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("Product price must be a number")

        if value <= 0:
            raise ValueError("Product price must be a positive number")

        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")

        if not value:
            raise ValueError("Description must contain text")

        self.__description = value

class Customer:
    """Customer class with getters and setters"""
    def __init__(self, surname, name, mobilePhone) :
        self.surname = surname
        self.name = name
        self.mobilePhone = mobilePhone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of surname!")

        if len(value) <= 1:
            raise ValueError("Surname must contain at least 2 characters")

        self.__surname = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")

        if len(value) <= 1:
            raise ValueError("Customer name must contain at least 2 characters")

        self.__name = value

    @property
    def mobilePhone(self):
        return self.__mobilePhone

    @mobilePhone.setter
    def mobilePhone(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of mobilePhone!")

        if len(value) != 10:
            raise ValueError("Wrong mobile phone format!")

        self.__mobilePhone = value

class Order:
    """Order class with add_product, del_product and sum_order methods"""
    def __init__(self, customer = None, productList = None) :
        if not isinstance(customer, Customer):
            raise TypeError("Wrong type of customer!")
        self.customer = customer

        if not all([isinstance(product, Product) for product in productList]) :
            raise TypeError("Wrong type of product!")
        self.productList = productList

    def add_product(self, newProduct):
        """A function that adds product to the total order"""
        if not isinstance(newProduct, Product):
            raise TypeError("Wrong type of product!")
        self.productList.append(newProduct)

    
    def del_product(self, product):
        """A function that delete product from the total order"""
        if not isinstance(product, Product):
            raise TypeError
        self.productList.remove(product)

    def sum_order(self):
        """
        Sum all prices
        A function that sum price of all products in order
        """
        result = 0
        for product in self.productList:
            result = result + product.price
        return result

    def __str__(self):
        return f'Customer: {self.customer.name}\nThe total order value:{self.sum_order()}'

xiaomi9 = Product("Xiaomi Redmi Note 9", 5000, "Some description")
xiaomiMi = Product("Xiaomi Mi 11 Ultra", 13500, "Some description")
customer = Customer("Shevchenko", "Vladyslav", "3961138687")
listOfProducts = [xiaomi9, xiaomiMi] 
obj3 = Order(customer, listOfProducts) 
obj3.add_product(xiaomi9)
print(obj3)
