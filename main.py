from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()

#creating a databsae
#conn = sqlite3.connect('inventory.db')
#creating cursor
#c = conn.cursor()

#commit changes
#conn.commit()


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
hlabel = Label(root, text = "Height entry: ")
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

    for record in record:
        print_records += str(record) + '\n'

    querylabel = Label(root, text = print_records)
    querylabel.grid(row = 5, column = 0, columnspan=2)
    conn.commit()
    conn.close()    
    return

sub_btn = Button(root, text = "Add records to database", command = submit)
sub_btn.grid(row = 3, column= 1, columnspan= 2, pady = 10, padx= 10, ipadx= 20)
out_btn = Button(root, text = "Show Records", command = output)
out_btn.grid(row = 4, column= 1, columnspan= 2, pady = 10, padx= 10, ipadx= 20)
#creatingsub_btn.grid(row = 3, column= 1, columnspan= 2, pady = 10, padx= 10, ipadx= 20) table

#c.execute('''
#          CREATE TABLE storage (
#          item_name text,
#          row integer,
#          height integer
#          )
#          ''')


#close connection
#conn.close()



root.mainloop()
