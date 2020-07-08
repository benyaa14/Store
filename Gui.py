from Store import *
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


def make_sale():
    mes=s.inputGui(txt_sale.get())
    messagebox.showinfo('Sale',mes)
def find_size():
    mes=s.inputSize(txt_find.get())
    messagebox.showinfo("here are relevant phones",mes)
def count_prod():
    mes=s.inputCount(var.get())
    messagebox.showinfo('total of',mes)
def total():
    messagebox.showinfo("Ido dog?",s.profit())

win = Tk()
win.title('Store Data')
win.geometry('500x500')
txt_sale = Entry(win)
txt_sale.grid(row=0, column=1)
txt_find = Entry(win)
txt_find.grid(row=1, column=1)


var=StringVar()
rad_phone = Radiobutton(win, text='phones', variable=var, value='Phone')
rad_ref = Radiobutton(win, text='refrigerator', variable=var, value='Refrigerator')
rad_all = Radiobutton(win, text='all', variable=var, value='Product')
rads = [rad_phone, rad_ref, rad_all]

i = 0
for rad in rads:
    rad.grid(row=2, column=i)
    i += 1

btn_sale = Button(win, text='make sale', command=make_sale)
btn_find = Button(win, text='find phone by size',command=find_size)
btn_count = Button(win, text='count number of products',command=count_prod)
btn_total = Button(win, text='get total',command=total)
btns = [btn_sale, btn_find, btn_count, btn_total]
i = 0
for btn in btns:
    btn.grid(row=i, column=3)
    i += 1


s=Store()
c=Coupon(Coupon.PERCENTAGE,4,1,"new year")
ross=s.cus_list.find_cus(12)
ross.add_coupon(c)
win.mainloop()
# p = Phone(5, "ap")
# r = Refrigerator()
# # print(p)
# # print(r)
# s = Store()
# # print(s)
# pl = s.find_phone_by_size(4.2, 6)
# # sl = s.make_sale(12, "Ipad3")
# # print(sl)
# s = Store()
# c = Coupon(Coupon.PERCENTAGE, 4, 1, "new year")
# ross = s.cus_list.find_cus(12)
# ross.add_coupon(c)
# s.make_sale(12, "Iphone8")
# s.make_sale(14, "Iphone8")
# s.make_sale(12, "Iphone2")
# s.make_sale(12, "big blue")
# sale_list = s.get_all_sales()
#
# for x in sale_list:
#     print(x)
# print(s.profit())
#
# s = Store()
# c = Coupon(Coupon.PERCENTAGE, 4, 1, "new year")
# ross = s.cus_list.find_cus(12)
# ross.add_coupon(c)
# s.make_sale(12, "Iphone8")
# s.make_sale(14, "Iphone8")
# s.make_sale(12, "Iphone2")
# s.make_sale(12, "big blue")
# s.make_sale(12, "big blue")
# pl = s.find_phone_by_size(4, 6)
# s.make_sale(12, 'gear')
# s.make_sale(12, 'gear')
# s.make_sale(12, 'gear')
# s.make_sale(12, 'gear')
# s.make_sale(12, 'gear')
# val = s.count_product(Refrigerator)
#
# print(val)

