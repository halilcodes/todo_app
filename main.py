todos = []

while True:
    user_action = input("Type add, show or exit: ").casefold().strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for todo in todos:
                print(todo.title())
        case 'exit':
            break
        case _:
            print('Unknown command!')

print('Bye!')
