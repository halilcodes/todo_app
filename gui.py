import PySimpleGUI as sg
import time
import functions

FONT = ('Helvetica', 20)
time_now = time.strftime("%b %d, %Y %H:%M:%S")

todos = functions.get_todos()

# Define the window's contents
sg.theme("Black")
show_time = sg.Text(f"Time is {time_now}")
label1 = sg.Text("Enter a To-Do")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button('Add')
listBox = sg.Listbox(values=todos, size=(20, 12), key='-LIST-')
editButton = sg.Button('Edit')
deleteButton = sg.Button('Delete')
quitButton = sg.Button('Quit')

layout = [
    [show_time],
    [label1],
    [inputBox, addButton],
    [listBox, editButton, deleteButton],
    [quitButton]
]

# Create the window
window = sg.Window('To-Do App', layout=layout, font=FONT)


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
    elif event == 'Edit':
        try:
            old_todo = values['-LIST-'][0]
            new_todo = values['todo'].title() + "\n"
            print(new_todo)
            print(old_todo)
            todos[todos.index(old_todo)] = new_todo
        except IndexError:
            continue
    elif event == 'Delete':
        try:
            del_todo = values['-LIST-'][0]
            del todos[todos.index(del_todo)]
        except IndexError:
            continue
    window['-LIST-'].update(values=todos)

functions.write_todos(todos)
print(todos)
# Finish up by removing from the screen
window.close()
