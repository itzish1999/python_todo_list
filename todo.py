# This is a to do list in which I will provide an explanation on how to do it and what the code does. Use this as a reference

""" First what you want to do is import the tkinter library. 
Tkinter is automatically shipped with Python so you don't have to install it.
Tkinter is a very popular and commonly use GUI library. """

# Importing the Tkinter library. What this piece of code is, is importing everything from the library
from tkinter import *
# Also importing an important widget from the Tkinter library called a message box which displays messages
import tkinter.messagebox

# Define todo list functions

# entertask() is used to add a task to the listbox.
def entertask():
    # A new window to pop up to take input
    input_text = ""
    # The add() function is called when the Add task button is clicked. Entered input is stored in input_text.
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title = "Warning!", message = "Please Enter Some Text")
        else:
            listbox_task.insert(END, input_text)
            # Close the root1 window
            root1.destroy()
    root1 = Tk()
    root1.title("Add Task")
    entry_task = Text(root1, width = 40, height = 4)
    entry_task.pack()
    button_temp = Button(root1, text = "Add A Task", command = add)
    button_temp.pack()
    root1.mainloop()

        

# Function to facilitate the delete task from the Listbox
def deletetask():
    # Selects the selected item and then deletes it
    selected = listbox_task.curselection()
    # delete() function is used to delete the item corresponding to the index in python to do list app.
    listbox_task.delete(selected[0])
# Executes this to mark completed

# Used to mark an item in to-do list as completed
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    # Store the text of selected item in a string
    temp_marked = listbox_task.get(marked)
    # Update it
    temp_marked = temp_marked+" ✔"
    # Delete it then insert it
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)

# Create a to-do list application window
# Tk() is a top level widget that we will use to create the main application window. We will build the application on it.
window = Tk()
# Giving a title via title() method
window.title("My Python To-Do list app")

# Creating the layout for our appliation

# The Frame() method is basically a container widget within our main window and will hold other widgets
frame_task = Frame(window)
""" The pack() method is geometry based and will organize the widget properly. 
Until explicitly mentioned, it will be presented in an orderly fashion. """
frame_task.pack()

# To hold items in a listbox
# Listbox() widget is going to store all tasks that we list. We gave three arguments about its style
listbox_task = Listbox(frame_task, bg = "black", fg = "white", height = 15, width = 50, font = "Roboto")
listbox_task.pack(side = tkinter.LEFT)

# Creating a scrollbar
# Scroll down in case the total list exceeds the size of the given window

# Scrollbar() widget places a scroll bar
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side = tkinter.RIGHT, fill = tkinter.Y)
listbox_task.config(yscrollcommand = scrollbar_task.set)
scrollbar_task.config(command = listbox_task.yview)

# Button widget

""" Button() widget is used to create a button.
We want the buttons in our to-do main list window so the input window is given, """
entry_button=Button(window, text = "Add a Task", width = 50, command = entertask)
entry_button.pack(pady = 3)

# Delete a Task Button
delete_button = Button(window, text = "Delete Selected Task", width = 50, command = deletetask)
delete_button.pack(pady = 3)

# Task completed button
mark_button = Button(window, text= "Mark as Completed", width = 50, command = markcompleted)
mark_button.pack(pady = 3)

# The window.mainloop() method displays and runs everything we have on our code
window.mainloop()