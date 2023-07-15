todos = []


def show_todos(todo_list):
    for num, do in enumerate(todo_list):
        print(f"{num}- {do.title()}", end="")
    print()


with open("todo_list.txt", "r", encoding="utf8") as file:
    for line in file:
        todos.append(line)

while True:
    user_action = input("Type add, show, edit or exit: ").casefold().strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"
            todos.append(todo)
            file = open("todo_list.txt", "w")
            file.writelines(todo)
            file.close()
        case 'show' | 'display':
            show_todos(todos)
        case 'edit':
            show_todos(todos)
            index = int(input("Select list item to edit: "))
            new_input = input("Enter new list item: ")
            print(f"{todos[index]} changed with {new_input}")
            todos[index] = new_input
        case 'exit':
            break
        case _:
            print('Unknown command!')

with open("todo_list.txt", "w", encoding="utf8") as file:
    for todo in todos:
        file.write(todo)
print('Bye!')
