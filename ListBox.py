from tkinter import * 
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
        
        
    print("Su orden es: ")
    #print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection())
    for index in  reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
