from tkinter import * 
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
        
        
