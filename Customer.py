import csv


class Customer:
    def __init__(self, data_list):  # id,first name,last name,home address,pohne number ,gender
        if data_list[5] not in ('M', 'F', 'male'):
            data_list[5] = 'F'
        elif data_list[5] == 'male':
            data_list[5] = 'M'
        self.id = str(data_list[0])
        self.f_name = data_list[1]
        self.l_name = data_list[2]
        self.adress = data_list[3]
        self.phone = str(data_list[4])
        self.gender = data_list[5]
        self.coupons=set()

    def get_cup_ids(self):
        if len(self.coupons)==0:
            return
        ids=[]
        for cup in self.coupons:
            ids.append(cup.get_pro_id())
        return ids

    def add_coupon(self,coupon):
        self.coupons.add(coupon)

    def get_fName(self):
        return self.f_name

    def get_lName(self):
        return self.l_name
    def get_id(self):
        return self.id

    def cus_details(self):
        return f"{self.f_name} {self.l_name}, {self.adress},{self.phone}, {self.gender}"

    def __str__(self):
        return f"{'-' * 20}\nid:{self.id}\nname: {self.f_name} {self.l_name}\n" \
               f"adress: {self.adress}\nphone: {self.phone}\ngender: {self.gender} "

    def __eq__(self, other):
        return self.id==other.id
    def __hash__(self):
        return hash(self.id)

class Customers_list:
    def __init__(self, file='custmer.csv'):
        self.customers_list = set()
        if file != 'empty':
            with open(file, newline='') as csvfile:  # csvfile = var
                customers = csv.reader(csvfile)
                next(customers)
                for customer in customers:
                    self.customers_list.add(Customer(customer))

    def print(self):
        print(self.__str__())

    def __str__(self):
        if len(self.customers_list)==0:
            return "No Customers"

        for customer in self.customers_list:
            back=f'All Customers:\n{"-"*20}\n'
            for customer in self.customers_list:
                back+=f"{customer.get_fName()} {customer.get_lName()}\n"
            return back
    def add_customer(self,customer):
        if customer not in self.customers_list:
            self.customers_list.add(customer)
            return True
        return False
    def remove_customer(self,customer):
        if customer in self.customers_list:
            self.customers_list.remove(customer)
    def print_cus_by_lName(self,lName):
        for customer in self.customers_list:
            if lName==customer.get_lName():
                print(customer)
    def find_cus(self, id):
        for customer in self.customers_list:
            if str(id)==customer.get_id():
                return customer
    def remove_all(self):
        self.customers_list=[]

class Coupon:
    SIMPLE_DIS='SIMPLE_DIS'
    PERCENTAGE='PERCENTAGE'
    def __init__(self,type,discount,pr_id,name,date="1/1/2020"):
        if type == Coupon.PERCENTAGE:
            if discount<0:
                discount=0
            elif discount>100:
                discount=100
        if type==Coupon.SIMPLE_DIS and discount<0:
            discount=0
        self.type=type
        self.discount=discount
        self.pr_id=str(pr_id)
        self.name=name
        self.date=date
    def get_pro_id(self):
        return self.pr_id
    def get_type(self):
        return self.type
    def get_discount(self):
        return self.discount
    def __eq__(self, other):
        return self.name==other.name

    def __hash__(self):
        return hash(self.name)
    def __str__(self):
        return f"{self.name}, {self.discount}"

# c1 = Customer(['123', 'ross', 'geller', 'budaphest', '054442222', "M"])
# c11=Customer(['123', 'rosis', 'geliler', 'budaiphest', '0544i42222', "M"])
# print(c1)
# print(c1.cus_details())
#
# c2 = Customers_list()
# c2.print()
#
# # c2.add_customer(c1)
# # c2.remove_customer(c1)
# # c2.remove_all()
# print(c2)
#
# c2.print_cus_by_lName('Tribbiani')
# print(c2.find_by_Id(18))
# print(c2)
#
# c=Coupon(Coupon.PERCENTAGE,-5,2,"new year")
# cup=Coupon(Coupon.SIMPLE_DIS,200,6,"new years")
# c1.add_coupon(c)
# c1.add_coupon(cup)
# # for cup in c1.coupons:
# #     print(cup)
# # print(c2.add_customer(c11))
# print(c2)