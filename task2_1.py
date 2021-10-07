class Product:
    def __init__(self, price, description, dimension) :
        self.__price = price
        self.__description = description
        self.__dimension = dimension

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def set_price(self, price):
        if(isinstance(price, float) and price > 0.0): 
            self.__price = price
        else: 
            raise Exception("Wrong input type or value")

    @property
    def description(self):
        return self.__description

    @description.setter
    def set_description(self, description):
        if(isinstance(description, str)): 
            self.__description = description
        else: 
            raise Exception("Wrong input type or value")
    
    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def set_description(self, dimension):
        if(isinstance(dimension, str)): 
            self.__description = dimension
        else: 
            raise Exception("Wrong input type or value")


class Customer:
    def __init__(self, surname, name, mobilePhone) :
        self.__surname = surname
        self.__name = name
        self.__mobilePhone = mobilePhone

    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def set_surname(self, surname):
        if(isinstance(surname, str)): 
            self.__price = surname
        else: 
            raise Exception("Wrong input type or value")

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        if(isinstance(name, str)): 
            self.__name = name
        else: 
            raise Exception("Wrong input type or value")
    
    @property
    def mobilePhone(self):
        return self.__mobilePhone

    @mobilePhone.setter
    def set_description(self, mobilePhone):
        if(isinstance(mobilePhone, str)): 
            self.__description = mobilePhone
        else: 
            raise Exception("Wrong input type or value")

class Order:
    def __init__(self, customer, product) :
        self.__customer = customer
        self.__product = product

    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def set_customer(self, customer):
        if(isinstance(customer, Customer)): 
            self.__customer = customer
        else: 
            raise Exception("Wrong input type or value")

    @property
    def product(self):
        return self.__product
    
    @product.setter
    def set_product(self, product):
        if(isinstance(product, Product)): 
            self.__product = product
        else: 
            raise Exception("Wrong input type or value")

    def count(self):
        result = []
        for y in self.__product:
            result.append(y.price * y.dimension)
        return sum(result) 


xiaomi9 = Product(5000, "Xiaomi Redmi Note 9", 2)
xiaomiMi = Product(13500, "Xiaomi Mi 11 Ultra", 1)
customer = Customer("Shevchenko", "Vladyslav", 961138687)

listOfProducts = [xiaomi9, xiaomiMi]
obj3 = Order(customer, listOfProducts)
obj4 = Order("customer", "price")
print(customer.name)
print(obj3.count())
