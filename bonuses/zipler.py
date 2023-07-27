import PySimpleGUI as sg
import zipfile
import pathlib


def make_archive(filepaths: list[str], dest_dir: str):
    final_dest = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(final_dest, 'w') as zipper:
        for path in filepaths:
            # zip_path = path.split("/")[-1]
            zip_path = pathlib.Path(path)
            zipper.write(zip_path, arcname=zip_path.name)   # convention to use pathlib not str


label1 = sg.Text("Select files to compress: ")
input1 = sg.Input(key='input')
button1 = sg.FilesBrowse("Choose", key="files")
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input(key='output')
button2 = sg.FolderBrowse("Choose", key="folder")
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
    destination_filepath = values['folder']
    target_filepath = values['files']
    if ";" in target_filepath:  # multiple selection made
        target_filepath = target_filepath.split(";")
    else:
        target_filepath = [target_filepath]
    make_archive(target_filepath, destination_filepath)

    print(target_filepath, "\n", destination_filepath)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break


window.close()