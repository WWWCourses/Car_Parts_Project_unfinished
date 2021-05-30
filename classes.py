from datetime import datetime


class Users:

    def __init__(self, role, first_name, last_name, email, phone_number, password, created=datetime.now()):
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.created = created

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def print_info(self):
        print(f'{self.role}: {self.first_name} {self.last_name}, {self.email}, {self.created}')


class Car_parts:

    def __init__(self, code, product_name, category, buying_price, client_price, application, manufacturer):
        self.code = code
        self.product_name = product_name
        self.category = category
        self.buying_price = buying_price
        self.client_price = client_price
        self.application = application
        self.manufacturer = manufacturer

    def buy_price(self):
        try:
            price = float(self.buying_price.replace(",", "."))
            return price
        except ValueError:
            return 0

    def sell_price(self):
        try:
            price = float(self.client_price.replace(",", "."))
            return price
        except ValueError:
            return 0

    def print_info(self):
        print("Code ", self.code)
        print("Name ", self.product_name)
        print("Category ", self.category)
        print("Price ", self.client_price)
        print("Application ", self.application)
        print("Manufacturer ", self.manufacturer)

    def __str__(self):
        return self.product_name


class Orders:

    def __init__(self, date, user, ordered_parts, total_costs, profit):
        self.date = date
        self.user = user
        self.ordered_parts = ordered_parts
        self.total_costs = total_costs
        self.profit = profit

    def __str__(self):
        return self.date
