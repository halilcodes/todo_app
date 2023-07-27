import PySimpleGUI as sg


def feet_meter(feet, inch):
    return (feet * 30.48 + inch * 2.54) / 100


layout = [
    [sg.Text("Enter feet: "), sg.InputText(key="feet")],
    [sg.Text("Enter inches: "), sg.InputText(key="inches")],
    [sg.Button('Convert'), sg.Button('Quit'), sg.Text(size=(40, 1), key='OUTPUT')]
]

window = sg.Window("feet meter", layout)

while True:
    event, values = window.read()
    try:
        if values['feet'] == "":
            ft = 0.0
        else:
            ft = float(values['feet'])
        if values['inches'] == "":
            inches = 0.0
        else:
            inches = float(values['inches'])
        result = feet_meter(ft, inches)
        statement = f"{result:.3f} m"
    except ValueError as e:
        # print(e)
        statement = "Enter valid numbers"
    window['OUTPUT'].update(statement)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break


window.close()