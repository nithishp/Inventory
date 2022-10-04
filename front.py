from tkinter import *
import db
db.db_works()
# create window
root = Tk()
root.title('Inventory')
root.geometry('500x500')
root.configure(bg="#C3E0E5")
#Displaying the labels
product_name = Entry(root,width=30,borderwidth=5)
product_price = Entry(root,width=30,borderwidth=5)
product_quantity = Entry(root,width=30,borderwidth=5)
product_name.grid(row=0,column=0,pady=5)
product_price.grid(row=1,column=0,pady=5)
product_quantity.grid(row=2,column=0,pady=5)
def add_btn():
    db.add_to_inventory(product_name.get(),product_quantity.get(),product_price.get())
    product_name.delete(0,END)
    product_price.delete(0,END)
    product_quantity.delete(0,END)
#Displaying the buttons
add = Button(root,text="Add",command=add_btn)
add.grid(row=3,column=0,pady=10)
delete = Button(root,text="Delete")
delete.grid(row=3,column=1,pady=10)
update = Button(root,text="Update")
update.grid(row=3,column=2,pady=10)
search = Button(root,text="Search")
search.grid(row=3,column=3,pady=10)
show = Button(root,text="Show")
show.grid(row=3,column=4,pady=10)
root.mainloop()
