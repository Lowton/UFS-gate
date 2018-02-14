from tkinter import *

def event():
    print('Кто-то крошит батон')

tk = Tk()
btn = Button(tk, text='Ткни в меня', command=event)
btn.pack()

