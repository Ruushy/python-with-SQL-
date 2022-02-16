from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('database.db')
c = conn.cursor()
class application:
    def __init__(self , master):
        self.master = master

        self.heading = Label(master, text = "update appoitmentt" ,fg = 'steelblue' , font = 'arial 40 bold')
        self.heading.place(x = 250 , y = 0)


        self.name = Label(master , text = "enter patiant's name " , fg = "steelblue" , font = "arial 20 bold")
        self.name.place(x = 0 , y = 100)


        self.name_en = Entry(master , width = 40 )
        self.name_en.place(x = 300 , y = 113)

        self.search = Button(master , text= "search" , width = 10 ,  bg = 'steelblue' , command = self.search_db)
        self.search.place(x = 360 , y = 150)

    
    def search_db(self):
        self.tes= self.name_en.get()

        sql = "SELECT * FROM hos WHERE name LIKE?"
        self.res = c.execute(sql ,(self.tes,))
        for self.row in self.res:
            self.nam = self.row[0]
            self.age = self.row[1]
            self.location = self.row[2]
            self.gender = self.row[3]
            self.ptime = self.row[4]

        self.uname = Label(self.master , text = " patiant's name" , font = 'arial 17 bold')
        self.uname.place(x = 10 , y = 200)

        self.uage = Label(self.master , text = "AGE "  , font = 'arial 17 bold' )
        self.uage.place(x = 10 , y = 240)

        self.ulocation = Label(self.master , text = " Locatin"  , font = 'arial 17 bold')
        self.ulocation.place(x = 10 , y = 280)

        self.ugender = Label(self.master , text = " Gender" , font = 'arial 17 bold')
        self.ugender.place(x = 10 , y = 320)

        self.uptime = Label(self.master , text = "appoitment time " , font = 'arial 17 bold')
        self.uptime.place(x = 10 , y = 360)



        self.un = Entry(self.master , width = 30)
        self.un.place(x = 200 , y = 210)
        self.un.insert(END , str(self.nam))

        self.ua = Entry(self.master , width = 30)
        self.ua.place(x = 200 , y = 250)
        self.ua.insert(END , str(self.age))

        self.ul = Entry(self.master , width = 30)
        self.ul.place(x = 200 , y = 290)
        self.ul.insert(END , str(self.location))

        self.ug = Entry(self.master , width = 30)
        self.ug.place(x = 200 , y = 330)
        self.ug.insert(END , str(self.gender))

        self.up = Entry(self.master , width = 30)
        self.up.place(x = 200 , y = 370)
        self.up.insert(END , str(self.ptime))


        self.update = Button(self.master , text = "update" , width = 20 , height = 2 , bg = 'lightblue' , command = self.updating)
        self.update.place(x = 210 , y = 400)
        self.dell = Button(self.master , text = "DELET" , width = 20 , height = 2 , fg = 'red' , command = self.deleting)
        self.dell.place(x = 80 , y = 400)

    def updating(self):
        self.val = self.un.get()
        self.val2 = self.ua.get()
        self.val3 = self.ul.get()
        self.val4 = self.ug.get()
        self.val5 = self.up.get()

        query = "UPDATE HOS set name = ? , age = ? , location = ? , gender = ? , ptime = ? WHERE name LIKE?"
        c.execute(query , (self.val , self.val2 , self.val3 , self.val4 , self.val5 , self.name_en.get()))
        conn.commit()
        tkinter.messagebox.showinfo(" " , 'succefuly updated')
   

    def deleting(self):

        sql2 = "DELETE FROM hos WHERE name LIKE ?"
        c.execute(sql2 , (self.name_en.get(),))
        conn.commit()
        tkinter.messagebox.showinfo(" " , 'succefuly deleted')
        self.un.destroy()
        self.ua.destroy()
        self.ul.destroy()
        self.ug.destroy()
        self.up.destroy()
        self.uname.destroy()
        self.uage.destroy()
        self.ulocation.destroy()
        self.ugender.destroy()
        self.uptime.destroy()
        

    
        









        
            





root = Tk()
b = application(root)

root.geometry("1350x750")

root.mainloop()
