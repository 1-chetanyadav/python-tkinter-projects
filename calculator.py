from tkinter import *

root = Tk()

root.geometry("280x400")
root.title("Complex Calculator")

# frame = Frame(root,pady=35,padx=35, bg="maroon")
# frame.pack()

def add_button(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    return

def clear_button():
    e.delete(0,END)

e = Entry(root, borderwidth=8, width=36)
#e.place(width=50,height=60)
e.grid(row=1, column=0, columnspan=7,ipady=12)

button_1 = Button(root, text="1", pady=25, padx=25, command=lambda: add_button(1))
button_2 = Button(root, text="2", pady=25, padx=25, command=lambda: add_button(2))
button_3 = Button(root, text="3", pady=25, padx=25, command=lambda: add_button(3))
button_4 = Button(root, text="4", pady=25, padx=25, command=lambda: add_button(4))
button_5 = Button(root, text="5", pady=25, padx=25, command=lambda: add_button(5))
button_6 = Button(root, text="6", pady=25, padx=25, command=lambda: add_button(6))
button_7 = Button(root, text="7", pady=25, padx=25, command=lambda: add_button(7))
button_8 = Button(root, text="8", pady=25, padx=25, command=lambda: add_button(8))
button_9 = Button(root, text="9", pady=25, padx=25, command=lambda: add_button(9))
button_0 = Button(root, text="0", pady=25, padx=25, command=lambda: add_button(0))
#button_dot = Button(root, text=".", pady=25, padx=25, command= add_button)

button_sum = Button(root, text="+", pady=25, padx=25, command=add_button())
button_sub = Button(root, text="-", pady=25, padx=25, command=add_button())
button_equal = Button(root, text="Clear", pady=25, padx=25, command = clear_button())
button_multi = Button(root, text="x", pady=25, padx=25, command=add_button())
button_div = Button(root, text="/", pady=25, padx=25, command=add_button())

button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)

button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)

button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)

button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)
button_sum.grid(row=4, column=4)
button_sub.grid(row=5, column=4)
button_multi.grid(row=2, column=4)

button_div.grid(row=3, column=4)
button_equal.grid(row=5, column=3)

root.mainloop()
