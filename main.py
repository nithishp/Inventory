from tkinter import *
from sqlite3 import *
#create database connection
conn = connect('inventory.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL)''')
#create window
root = Tk()
root.title('Inventory')
root.geometry('500x500')
root.configure(bg="#C3E0E5")

def add_to_inventory():
    print("Adding to inventory")
    id = 0
    c.execute('''INSERT INTO inventory (id , name , quantity , price) VALUES ({}, {} , {}, {})'''.format(id , product_name.get() , product_quantity.get() , product_price.get()))
    id = id+1
    c.execute('''select * from inventory''')
    for row in c.fetchall():
        print(row)

    conn.commit()

def delete_from_inventory():
    print("Deleting from inventory")
    # c.execute('''DELETE FROM inventory WHERE id = {}'''.format(product_id.get()))
    # conn.commit()
def update_inventory():
    print("Updating inventory")
def search_inventory():
    print("Searching inventory")
    # c.execute('''SELECT * FROM inventory WHERE name = '{}' '''.format(product_name.get()))
    # for row in c.fetchall():
    #     print(row)
    # c.execute('''SELECT * FROM inventory WHERE name = '{}' '''.format(product_name.get()))
def show_inventory():
    print("Showing inventory")
    # c.execute('''SELECT * FROM inventory''')
    # for row in c.fetchall():
    #     print(row)

#Displaying the labels
product_name = Entry(root,width=30,borderwidth=5)
product_price = Entry(root,width=30,borderwidth=5)
product_quantity = Entry(root,width=30,borderwidth=5)
product_name.grid(row=0,column=0,pady=5)
product_price.grid(row=1,column=0,pady=5)
product_quantity.grid(row=2,column=0,pady=5)
add = Button(root,text="Add",command=add_to_inventory)
add.grid(row=3,column=0,pady=10)
delete = Button(root,text="Delete",command=delete_from_inventory)
delete.grid(row=3,column=1,pady=10)
update = Button(root,text="Update",command=update_inventory)
update.grid(row=3,column=2,pady=10)
search = Button(root,text="Search",command=search_inventory)
search.grid(row=3,column=3,pady=10)
show = Button(root,text="Show",command=show_inventory)
show.grid(row=3,column=4,pady=10)
root.mainloop()

