from tkinter import *

def submit():
    print("Allowed")


root = Tk()
topFrame = Frame(root)
#topFrame.pack()
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row = 0, sticky = E)
label_2.grid(row = 1, sticky = E)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan = 2)

sub = Button(root, text = "Submit" , command = submit)
sub.grid(row = 3, columnspan = 2)

#theLabel.pack()
root.mainloop()