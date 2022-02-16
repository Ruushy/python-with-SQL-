from tkinter import *
import sqlite3 
import tkinter.messagebox
conn = sqlite3.connect('database.db')
c = conn.cursor()
class application:
    def __init__(self , master):
       self.master = master


       self.left = Frame(master , width = 800 , height = 720 , bg = 'white' )
       self.left.pack(side = LEFT)

       self.right = Frame(master , width = 400 ,  height = 720 ,bg = 'blue' )
       self.right.pack(side = RIGHT)
       self.box = Text(self.right ,  width = 60 , height = 40)
       self.box.place(x = 50 , y = 30)

       self.heading = Label(self.left , text = "hospital managment " ,font = ('arial 40 bold') , fg = 'black')
       self.heading.place( x = 100, y = 0)
       

    
       self.name = Label(self.left , text = "Name " , font = ('arial 15 bold'), fg = 'black')
       self.name.place( x =  10 , y = 100)

       
       self.age = Label(self.left , text = "age " , font = ('arial 15 bold'), fg = 'black')
       self.age.place( x =  10 , y = 150)

       self.location = Label(self.left , text = "location " , font = ('arial 15 bold'), fg = 'black')
       self.location.place( x =  10 , y = 210)
       
       self.gender = Label(self.left , text = "gender " , font = ('arial 15 bold'), fg = 'black')
       self.gender.place( x =  10 , y = 260)

       

       self.aptime = Label(self.left , text = "appoitment time " , font = ('arial 15 bold'), fg = 'black')
       self.aptime.place( x =  10 , y = 310)

       self.name_en = Entry(self.left , width = 30)
       self.name_en.place( x =  200 , y = 100)

       self.age_en = Entry(self.left , width = 30)
       self.age_en.place( x =  200 , y = 150)

       self.location_en = Entry(self.left , width = 30)
       self.location_en.place( x =  200 , y = 210)

       self.gender_en = Entry(self.left , width = 30)
       self.gender_en.place( x =  200 , y = 260)

       self.aptime_en = Entry(self.left , width = 30)
       self.aptime_en.place( x =  200 , y = 310)
     
       self.sub = Button(self.left , text = 'add appoitment' ,font = 'arial 15 bold' ,fg = 'black' , command = self.add_apoitment)
       self.sub.place(x = 230 , y = 380)

    def add_apoitment(self):
           self.val1 = self.name_en.get()
           self.val2 = self.age_en.get()
           self.val3 = self.location_en.get()
           self.val4 = self.gender_en.get()
           self.val5 = self.aptime_en.get()
           if self.val1 == '' or self.val2 =='' or self.val3 == '' or self.val4 == '' or self.val5 == '':
               tkinter.messagebox.showinfo(" " , "fill the planks" )
           else:
               sql = "INSERT INTO 'hos' (name , age , location , gender , ptime ) VALUES(? , ? , ? , ? , ?)"
               c.execute(sql,(self.val1 , self.val2, self.val3 , self.val4 , self.val5))
               conn.commit()
               tkinter.messagebox.showinfo("succes " ,"succesfully created appoitment for ")
               self.box.insert(END , "apoitment fixed")
               
           

root = Tk()
b = application(root)

root.geometry("1290x720+0+0")

#root.resizable(false , false)

root.mainloop()
