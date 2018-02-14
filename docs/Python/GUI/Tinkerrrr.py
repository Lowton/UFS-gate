import tkinter
import math

def Square(radius):      
  return math.pi * radius**2 

def calculate_square():
  radius = float(radius_entry.get())
  try:
    square = "%11.3f" % Square(radius)
  except:
    square = "?"
  square_label.configure(text=square)

root = tkinter.Tk()
root.title("Площадь круга")
frame = tkinter.Frame(root)
frame.pack()
radius_entry = tkinter.Entry(frame, width=10)
radius_entry.grid(row=0, column=0)
square_label = tkinter.Label(frame, text="?")
square_label.grid(row=0, column=1)
eval_button = tkinter.Button(frame, text="Calculate", width=10,
                     command=calculate_square)
eval_button.grid(row=1, column=0)
exit_button = tkinter.Button(frame, text="Exit", width=10,
                     command=root.destroy)
exit_button.grid(row=1, column=1)
root.mainloop()
