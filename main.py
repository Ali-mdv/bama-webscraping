from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from func import *


#================================================FUNCTION=========================================
def display_selected_item_index(event):
    brands_car_combobox.set('')
    brands_car_combobox["value"] = (car_brands(car_var.get()))
    brands_car_combobox.current()


def search_buttom(car,car_brand,from_year,to_year,price,installment,replacement,listbox_show_car):
    listbox_show_car.delete(0, END)
    listbox_show_info_car.delete(0, END)
    get_car_title(car,car_brand,from_year,to_year,price,installment,replacement,listbox_show_car)
    messagebox.showinfo("showinfo", f"{listbox_show_car.size()} پیدا شد.")


def click_from_year(event):
    if from_year_entry.get() == 'از سال':
        from_year.set('')


def click_to_year(event):
    if to_year_entry.get() == 'تا سال':
        to_year.set('')


def double_click(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        listbox_show_info_car.delete(0, END)
        get_car_detail(index,listbox_show_info_car)

#================================================FUNCTION=========================================







#================================================GUI=========================================
window = Tk()
window.title('Bama')
window.geometry('505x590')
window.geometry('650x650')
window.resizable(width=0,height=0)
window.configure(bg='white')

icon = PhotoImage(file = 'bama.png')
window.iconphoto(False, icon)




#================================================VAR=========================================
car_var = StringVar()
car_var.set('همه برند ها')

car_brand_var = StringVar()
car_brand_var.set('همه مدل ها')

from_year = StringVar()
to_year = StringVar()

price_var = BooleanVar()
installment_var = BooleanVar()
replacement_var = BooleanVar()
#================================================VAR=========================================



#================================================Listbox=========================================
listbox_show_car = Listbox(window,width=40,height=13,justify='right')
listbox_show_car.grid(row = 2,column = 0,columnspan = 5,sticky = E+W,padx = (10,27),pady = (5,0))
listbox_show_car.bind("<Double-Button-1>", double_click)

listbox_show_info_car = Listbox(window,width=40,height=17,justify='right')
listbox_show_info_car.grid(row = 4,column = 0,columnspan = 5,sticky = E+W,padx = (10,27),pady = (5,0))
#================================================Listbox=========================================



#================================================BUTTOM=========================================
buttom_search = Button(window,text = 'Search', command = lambda:
                search_buttom(car_var.get(),car_brand_var.get(),from_year.get(),to_year.get(),
                                price_var.get(),installment_var.get(),replacement_var.get(),
                                listbox_show_car))
buttom_search.grid(row = 0,column = 0,rowspan = 2,sticky = E+W+N+S,padx = (10,5))
#================================================BUTTOM=========================================



#================================================Scrollbar=========================================
scroll_y = Scrollbar(window,orient="vertical")
scroll_y.grid(column=0,row=2,padx=(5,5),pady=(5,5),columnspan = 5,sticky=E+N+S)
listbox_show_car.config(yscrollcommand=scroll_y.set)
scroll_y.config(command=listbox_show_car.yview)
scroll_x = Scrollbar(window,orient='horizontal')
scroll_x.grid(row=3,padx=(10,10),pady=(0,5),sticky=E+W,columnspan =5)
listbox_show_car.config(xscrollcommand=scroll_x.set)
scroll_x.config(command=listbox_show_car.xview)


scroll_y = Scrollbar(window,orient="vertical")
scroll_y.grid(column=0,row=4,padx=(5,5),pady=(5,5),columnspan = 5,sticky=E+N+S)
listbox_show_info_car.config(yscrollcommand=scroll_y.set)
scroll_y.config(command=listbox_show_info_car.yview)
scroll_x = Scrollbar(window,orient='horizontal')
scroll_x.grid(row=5,padx=(10,10),pady=(0,5),sticky=E+W,columnspan =5)
listbox_show_info_car.config(xscrollcommand=scroll_x.set)
scroll_x.config(command=listbox_show_info_car.xview)
#================================================Scrollbar=========================================



#================================================Combobox=========================================
all_car_combobox = ttk.Combobox(window,textvariable = car_var,width = 20)
all_car_combobox["value"] = (all_car_brands(all_car_combobox))
all_car_combobox.grid(row = 0,column = 4,padx =(25,10),sticky = W)
all_car_combobox.current()
all_car_combobox.bind("<<ComboboxSelected>>", display_selected_item_index)  


brands_car_combobox = ttk.Combobox(window,textvariable = car_brand_var,width = 20)
brands_car_combobox.grid(row = 1,column = 4,padx =(25,10),sticky = W)
#================================================Combobox=========================================



#================================================Entry===========================================
from_year_entry= Entry(window,textvariable=from_year,width=10,justify='right')
from_year_entry.grid(row = 0,column = 3,padx = (2,5),sticky = E)
# from_year_entry.bind("<Button>", click_from_year)


to_year_entry = Entry(window,textvariable=to_year,width=10,justify='right')
to_year_entry.grid(row = 1,column = 3,padx = (2,5),sticky = E)
# to_year_entry.bind("<Button>", click_to_year)
#================================================Entry===========================================



#================================================Checkbutton=========================================
price_chk_btn = Checkbutton(window,text = 'قیمت دار',variable =price_var)
price_chk_btn.grid(row = 0,column = 2,padx = (5,5),sticky = E+W)

installment_chk_btn = Checkbutton(window,text = 'اقساطی',variable =installment_var)
installment_chk_btn.grid(row = 1,column = 2,padx = (5,5),sticky = E+W)

replacement_chk_btn = Checkbutton(window,text = 'قابل معاوضه',variable =replacement_var)
replacement_chk_btn.grid(row = 1,column = 1,padx = (10,5),sticky = E+W)
#================================================Checkbutton=========================================




window.mainloop()
#================================================GUI=========================================
