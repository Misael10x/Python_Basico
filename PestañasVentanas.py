from tkinter import * 
from tkinter import ttk

window = Tk()

noteboock = ttk.Notebook(window)
noteboock.pack(expand=TRUE, fill='both')

tab1 = Frame(noteboock)
tab2 = Frame(noteboock)
tab3 = Frame(noteboock)

noteboock.add(tab1, text='Tab1')
noteboock.add(tab2, text='Tab2')
noteboock.add(tab3, text='Tab3')
