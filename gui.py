import PySimpleGUI as sg
import time
import functions

FONT = ('Helvetica', 20)
time_now = time.strftime("%b %d, %Y %H:%M:%S")

# Define the window's contents
show_time = sg.Text(f"Time is {time_now}")
label1 = sg.Text("Enter a To-Do")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
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

todos = functions.get_todos()

while True:
    event, values = window.read()

    print("event: ", event)
    print("values: ", values)
    print("-" * 20)
    if event == 'Quit' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Add':
        new_todo = values['todo'].title() + "\n"
        todos.append(new_todo)


functions.write_todos(todos)
print(todos)
# Finish up by removing from the screen
window.close()
