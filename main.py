
from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()



# Delete Entry Widget and Label
delete_entry = Entry(root, width=30)
delete_entry.grid(row=8, column=1, padx=20)
delete_label = Label(root, text="Delete by Item Name:")
delete_label.grid(row=8, column=0, padx=20)

# Delete Button and Function
def delete_record():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Get the item name to be deleted from the entry widget
    delete_term = delete_entry.get()

    # Delete records that match the specified item name
    c.execute("DELETE FROM storage WHERE item_name=?", (delete_term,))
    conn.commit()
    conn.close()

delete_btn = Button(root, text="Delete Record", command=delete_record)
delete_btn.grid(row=8, column=2)

search_entry = Entry(root, width=30)
search_entry.grid(row=6, column=1, padx=20)
search_label = Label(root, text="Search by Item Name:")
search_label.grid(row=6, column=0, padx=20)

# Search Button and Function
def search():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Get the search term from the entry widget
    search_term = search_entry.get()

    # Query the database for records matching the search term
    c.execute("SELECT * FROM storage WHERE item_name LIKE ?", ('%' + search_term + '%',))
    records = c.fetchall()

    # Display the search results
    search_results = ''
    for record in records:
        search_results += f"Item Name: {record[0]}, Row: {record[1]}, Column: {record[2]}\n"

    result_label = Label(root, text=search_results)
    result_label.grid(row=7, column=0, columnspan=2)

    conn.close()

search_btn = Button(root, text="Search", command=search)
search_btn.grid(row=6, column=2)

#creating a databsae
#conn = sqlite3.connect('inventory.db')
#creating cursor
#c = conn.cursor()

#commit changes
#conn.commit()

#add part number
#add items add 

#entry widgets
tentry = Entry(root, width = 30)
tentry.grid(row = 0, column = 1, padx = 20)
rentry = Entry(root, width = 30)
rentry.grid(row = 1, column= 1, padx = 20)
hentry = Entry(root, width = 30)
hentry.grid(row = 2, column = 1, padx = 20)

#widget labels
tlabel = Label(root, text = "Item entry: ")
tlabel.grid(row = 0, column=0, padx= 20)
rlabel = Label(root, text = "Row entry: ")
rlabel.grid(row = 1, column = 0, padx = 20)
hlabel = Label(root, text = "Column entry: ")
hlabel.grid(row = 2, column = 0, padx = 20)

#submit button and function
def submit():

    #connecting to db
    
    conn = sqlite3.connect('inventory.db')

    c = conn.cursor()   

    c.execute("INSERT INTO storage VALUES (:f_name, :f_row, :f_height)",
              {
                  'f_name': tentry.get(),
                  'f_row': rentry.get(),
                  'f_height': hentry.get()
              })

    conn.commit()

    tentry.delete(0, END)
    rentry.delete(0,END)
    hentry.delete(0,END)
    
    conn.close()

    return

def output():
    
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    #query db
    c.execute("SELECT *, oid FROM storage")
    record = c.fetchall()
    print(record)

    #run thru results
    print_records = ''

    for record in record[0]:
        print_records += str(record) + '\n'

    querylabel = Label(root, text = print_records)
    querylabel.grid(row = 5, column = 0, columnspan=2)
    conn.commit()
    conn.close()    
    return

sub_btn = Button(root, text = "Add records to database", command = submit)
sub_btn.grid(row = 10, column= 1, columnspan= 2, pady = 10, padx= 10, ipadx= 20)

#creatingsub_btn.grid(row = 3, column= 1, columnspan= 2, pady = 10, padx= 10, ipadx= 20) table

#c.execute('''
 #         CREATE TABLE storage (
  #        item_name text,
   #       row integer,
    #      height integer
     #     )
      #    ''')


#close connection
#conn.close()



root.mainloop()
