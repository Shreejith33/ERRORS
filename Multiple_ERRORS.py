# Multiple ERRORS!!!
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x400")
list_name = ["Mickey mouse", "Elsa", "Anna", "Donald duck"]
dict_student = { "name" : "Shreejith",
                 "age" : "11"}

try:
    print(list_name[5])
    
    print(dict_student["mom"])
    
except IndexError :
    messagebox.showinfo("Error", "This index does not exist")
except KeyError:
    messagebox.showinfo("Error","This key does not exist")
    
root.mainloop()