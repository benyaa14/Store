from Products import *

class Sale:
    def __init__(self, customer_id, prod_id, price, date=""):
        self.customer_id = customer_id
        self.prod_id = prod_id
        self.price = price
        self.date = date
    def get_price(self):
        return self.price
    def __str__(self):
        return f"{self.price}, {self.prod_id}, {self.customer_id}"


class Store:
    def __init__(self, file_name="custmer.csv", phone_file="phone.csv", ref_file="refrigerator.csv"):
        self.cus_list = Customers_list(file_name)
        self.products=Product_list()
        self.products.load_from_file(phone_file)
        self.products.load_from_file(ref_file)
        self.sales_order=[]

    def inputGui(self,input):
        input=str(input).strip()
        index=input.find(' ')
        cus_id=input[:index].strip()
        prod_name=input[index:].strip()

        mes=self.make_sale(cus_id,prod_name)
        if mes==False:
            return "fail to make this sale"
        else:
            return mes

    def inputCount(self,input):
        if input=='Refrigerator':
            return self.count_product(Refrigerator)
        elif input == 'Phone':
            return self.count_product(Phone)
        else:
            return self.count_product(Product)

    def inputSize(self,input):
        input=input.strip()
        index=input.find(' ')
        mini=input[:index].strip()
        maxi=input[index:].strip()
        return self.find_phone_by_size(float(mini),float(maxi))

    def find_phone_by_size(self,mini,maxi):
            maxi,mini=(float(max([mini,maxi])),float(min([mini,maxi])))
            found=[]
            for prod in self.products.products:
                if isinstance(prod,Phone):
                    if mini<=prod.get_screen_size()<=maxi:
                        found.append(prod)
            back=Product_list()
            for phone in found:
                back.add_prod(phone)
            return back

    def make_sale(self, cus_id, prod_name):
        if not self.cus_list.find_cus(cus_id) or not self.products.find_by_name(prod_name):
            return False

        cus = self.cus_list.find_cus(cus_id)
        prod = self.products.find_by_name(prod_name)
        cup_ids = cus.get_cup_ids()
        price = [prod.get_price()]
        if len(cus.coupons) == 0:
            self.products.make_sell(prod_name)
        elif prod.get_id() not in cup_ids:
            self.products.make_sell(prod_name)
        else:  # There is at least one relevant coupon
            for coup in cus.coupons:
                if coup.get_type() == Coupon.SIMPLE_DIS:
                    newPrice = price[0] - coup.get_discount()
                    if newPrice < 0:
                        newPrice = 0
                    price.append(newPrice)
                elif coup.get_type() == Coupon.PERCENTAGE:
                    newPrice = price[0] * (1 - (coup.get_discount() / 100))
                    price.append(newPrice)
            self.products.make_sell(prod_name)
        sale=Sale(cus_id, prod.get_id(), min(price))
        self.sales_order.append(sale)
        return sale
    def profit(self):
        profit=0
        if len(self.sales_order)==0:
            return profit
        for sale in self.sales_order:
            profit+=sale.get_price()
        return profit

    def get_all_sales(self):
        return self.sales_order

    def count_product(self,typo):
        counter=0
        for product in self.products.products:
            if isinstance(product,typo):
                counter+=product.get_quantity()
        return counter

    def __str__(self):
        back = "Store\n"
        back += self.products.__str__()
        back += '\n'
        back += self.cus_list.__str__()
        return back


# pro1=Product(123,'Ip',1,100,'a')
# pro2=Product(123,'Ipp',200,100,'a')
#
# p=Product("42","koalaFinder",1,100000,"bestAnimal")
# print(p)
# pl=Product_list()
# pl.load_from_file("proudact.csv")
# print(pl.add_prod(p))
# print(pl.add_prod(p))
# pl.add_prod(pro1)
# print(pl)
# print(pl.make_sell("koalaFindeer"))
# print(pl.make_sell("Gear2"))
# print(pl.make_sell("Ipad3"))
# print(pl)



# print(pl)
# s = Store()
# c = Coupon(Coupon.PERCENTAGE, 50, 2, "new year")
# c2 = Coupon(Coupon.SIMPLE_DIS, 70, 2, "new years")
# ross = s.cus_list.find_cus(12)
# ross.add_coupon(c)
# ross.add_coupon(c2)

s=Store()
s.inputGui("12 Iphone8")
# s.make_sale(12, 'Iphone8')
print(s.count_product(Phone))
# # print(s.inputSize("0 2"))
# s.make_sale(12,'Iphone8')
# print(s.count_product(Phone))