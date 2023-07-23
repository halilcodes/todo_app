import PySimpleGUI as sg
import time

time_now = time.strftime("%b %d, %Y %H:%M:%S")

# Define the window's contents
layout = [
    [sg.Text(f"Time is {time_now}")],
    [sg.Text("Enter a To-Do?")],
    [sg.InputText(key='-INPUT-', tooltip="Enter todo")],
    [sg.Text(size=(40, 1), key='-OUTPUT-')],
    [sg.Button('Ok'), sg.Button('Quit')]
]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
