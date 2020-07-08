from Customer import *
#mdmdkdkd

class Product:
    def __init__(self, id, name, quantity, price, producer):
        self.id = id
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)
        self.producer = producer

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price

    def reduce(self):
        if self.quantity > 1:
            self.quantity -= 1

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.get_name()

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"inventory= {self.quantity}, price= {self.price}, id= {self.id}"

class Refrigerator(Product):
    def __init__(self,number_of_doors=2,size=500,id=1,name="",inventory=10,price=100,manufacturer=""):
        super().__init__(id,name,inventory,price,manufacturer)
        self.number_of_doors=number_of_doors
        self.size=float(size)
    def __str__(self):
        back=f'Refrigerator: of size {self.size}, {super().__str__()}'
        return back

class Phone(Product):
    def   __init__(self,screen_size=5,os="",id=1,name="",inventory=10,price=100,manufacturer="Apple"):
        super().__init__(id,name,inventory,price,manufacturer)
        self.screen_size=float(screen_size)
        self.os=os
    def __str__(self):
        back=f'Phone: with size {self.screen_size}, os={self.os}, {super().__str__()}'
        return back
    def get_screen_size(self):
        return self.screen_size


class Product_list:
    def __init__(self):
        self.products = set()

    def add_prod(self, prod):
        if prod.get_quantity() <= 0:
            return False
        if prod not in self.products:
            self.products.add(prod)
            return True
        return False


    def find_by_name(self, name):
        for prod in self.products:
            if name == prod.get_name():
                return prod

    def make_sell(self, name):
        if self.find_by_name(name):
            prod = self.find_by_name(name)
            if prod.get_quantity() == 1:
                self.products.remove(prod)
                return True
            prod.reduce()
            return True
        return False

    def __str__(self):
        if len(self.products) == 0:
            return "Empty"
        back = f"All Products\n{'-' * 20}\n"
        for prod in self.products:
            back += f"{prod}\n"
        return back

    def load_from_file(self, file='proudact.csv'):
        if file=='empty':
            return
        with open(file, newline='') as csvfile:  # csvfile = var
            products = csv.reader(csvfile)
            var=next(products)
            if var[-1]=='os':
                for product in products:#id,name,inventory,price,manufacturer,screen size,os
                    self.products.add(Phone(os=product[6],id=product[0],name=product[1],
                                            inventory=product[2],price=product[3],
                                            manufacturer=product[4],screen_size=product[5]))
            elif var[-1]=='size':
                for product in products:  #id,name,inventory,price,manufacturer,number of doors,size
                    self.products.add(Refrigerator(number_of_doors=product[5], id=product[0], name=product[1],
                                            inventory=product[2], price=product[3],
                                            manufacturer=product[4], size=product[6]))

            else:
                for product in products:  # id,name,inventory,price,manufacturer
                    self.products.add(Product(product[0], product[1], product[2], product[3], product[4]))


