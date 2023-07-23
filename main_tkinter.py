from functions import get_todos, show_list
import time
import tkinter as tk

window = tk.Tk()
window.title("To Do App")
window.geometry("640x480")


todos = get_todos()
print(todos)
time_now = time.strftime("%b %d, %Y %H:%M:%S")
text_ = f"It is {time_now}"
time_label = tk.Label(window, text=text_)
time_label.grid(row=0, column=0, sticky="w")

presentation_label = tk.Label(window, text="Enter a To-Do: ")
presentation_label.grid(row=1, column=0)

textBox = tk.Text(window, height=1, width=50)
textBox.grid(row=2, column=0)

addButton = tk.Button(window, text="Add")
addButton.grid(row=2, column=1, padx=30)

todoBox = tk.Listbox(window)
todoBox.insert(tk.END, *todos)
todoBox.grid(row=3, column=0, sticky="w")


print(f"It is: {time_now}")

print('Bye!')

window.mainloop()
