from functions import get_todos, show_list
import time

todos = get_todos()
time_now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is: {time_now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ").casefold().strip()
    if user_action.startswith('add'):
        if user_action > 'add':
            todo = user_action[4:].strip().title() + "\n"
            todos.append(todo)
        else:
            todo = input('Enter a todo: ') + "\n"
            todos.append(todo)
        # with open("todo_list.txt", "a", encoding="utf8") as file:
        #     file.writelines(todo)
    elif user_action.startswith('show'):
        show_list(todos)
    elif user_action.startswith('edit'):
        show_list(todos)
        try:
            index = int(user_action[5:])
        except ValueError:
            index = int(input("Select list item to edit: "))
        new_input = input("Enter new list item: ") + "\n"
        print(f"{todos[index]} changed with {new_input}")
        todos[index] = new_input

    elif user_action.startswith('complete'):
        show_list(todos)
        try:
            index = int(input("Select list item that you completed: "))
            todos.pop(index)
        except (ValueError, IndexError):
            print("Invalid input.")
            continue
    elif user_action == "exit":
        break
    else:
        print('Unknown command!')

with open("todo_list.txt", "w", encoding="utf8") as file:
    file.writelines(todos)
print('Bye!')
