todos = []


def show_todos(todo_list):
    for num, do in enumerate(todo_list):
        print(f"{num}- {do.title()}")


while True:
    user_action = input("Type add, show, edit or exit: ").casefold().strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
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

print('Bye!')
