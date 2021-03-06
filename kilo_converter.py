from tkinter import *

window = Tk()

def kilo_converter():
    grames = float(e1_value.get())*1000
    t1.delete("1.0", END) # Deletes the content of the Text box when user input changes
    t1.insert(END, grames)
    pounds = float(e1_value.get())*2.20462
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    onces = float(e1_value.get())*35.274
    t3.delete("1.0", END)
    t3.insert(END, onces)

# Create a button widget
# The kilo_converter() function is called when the button is pushed
b1 = Button(window, text = "Convert", command = kilo_converter)
b1.grid(row = 1, column = 3)

# Create a Label widget with "Kg" as label
e0 = Label(window, text = "Kg")
e0.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value) # Create an Entry box for users to enter the value
e1.grid(row = 0, column = 1)

# Create three empty text boxes, t1, t2, and t3
t1 = Text(window, height =1, width = 15)
t1.grid(row = 1, column = 0)
t2 = Text(window, height =1, width = 15)
t2.grid(row = 1, column = 1)
t3 = Text(window, height =1, width = 15)
t3.grid(row = 1, column = 2)

# This makes sure to keep the main window open
window.mainloop()