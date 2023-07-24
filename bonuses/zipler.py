import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input(key='input')
button1 = sg.FilesBrowse("Choose")
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input(key='output')
button2 = sg.FolderBrowse("Choose")
ok_button = sg.Button('Compress')
quit_button = sg.Button('Quit')


layout = [
    [label1, input1, button1],
    [label2, input2, button2],
    [ok_button, quit_button]
]

window = sg.Window("Zipleyici", layout)

while True:
    event, values = window.read()
    print(event, values)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break


window.close()