import PySimpleGUI as sg
import time
import functions

FONT = ('Helvetica', 20)
time_now = time.strftime("%b %d, %Y %H:%M:%S")

# Define the window's contents
show_time = sg.Text(f"Time is {time_now}")
label1 = sg.Text("Enter a To-Do")
inputBox = sg.InputText(tooltip="Enter todo")
addButton = sg.Button('Add')
quitButton = sg.Button('Quit')

layout = [
    [show_time],
    [label1],
    [inputBox, addButton],
    [quitButton]
]

# Create the window
window = sg.Window('To-Do App', layout=layout, font=FONT)
event, values = window.read()

print(event)
print(values)
print("hello world!")

# Finish up by removing from the screen
window.close()
