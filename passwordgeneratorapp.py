from tkinter import *
import secrets
import string

window = Tk()

window.title('Password')
window.geometry('500x400')

def password():
    a = string.ascii_letters
    b = a + string.digits
    c = a + string.digits + string.punctuation
    lenght = int(e_value.get())
    passworda = "".join(secrets.choice(a) for x in range(lenght))
    passwordb = "".join(secrets.choice(b) for x in range(lenght))
    passwordc = "".join(secrets.choice(c) for x in range(lenght))

    # This is how the checkboxes work
    if (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0):
        t1.delete("1.0", END)  # Deletes the content of the Text box when user input changes
        t1.insert(END, passworda)
    elif (var2.get() == 1) and (var1.get() == 0) and (var3.get() == 0):
        t1.delete("1.0", END) 
        t1.insert(END, passwordb)
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1):
        t1.delete("1.0", END) 
        t1.insert(END, passwordc)
    else:
        t1.delete("1.0", END)  
        t1.insert(END, "Please, select just one option")

# Create a button widget
# The password() function is called when the button is pushed
b1 = Button(window, text = "Get password", command = password, height =2, width = 15)
b1.grid(row = 4, column = 6)

# Create a Label widget asking the number of characters as label
e0 = Label(window, text = "How many characters do you want in your password?", height =1, width = 45)
e0.grid(row = 0, column = 0)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

e1 = Checkbutton(window, text = "Just letters", variable = var1, onvalue=1, offvalue=0)
e1.grid(row = 1, column = 0, sticky = W)

e2 = Checkbutton(window, text = "Numbers and letters", variable = var2, onvalue=1, offvalue=0)
e2.grid(row = 2, column = 0, sticky = W)

e3 = Checkbutton(window, text = "Letters, numbers and special characters", variable = var3, onvalue=1, offvalue=0) 
e3.grid(row = 3, column = 0, sticky = W)

e_value = StringVar()
e = Entry(window, textvariable = e_value) # Create an Entry box for users to enter the value
e.grid(row = 0, column = 6)

# Create one empty text boxes
t1 = Text(window, height =1, width = 35)
t1.grid(row = 4, column = 0)


# This makes sure to keep the main window open
window.mainloop()
