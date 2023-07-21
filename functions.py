FILEPATH = "todos.txt"


def show_list(todo_list):
    print(todo_list)
    for num, do in enumerate(todo_list):
        print(f"{num}- {do.title()}", end="")
    print()


def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r+", encoding="utf8") as f:
            return f.readlines()
    except FileNotFoundError:
        with open(filepath, "w", encoding="utf8") as _:  # create the file if not exists.
            return []


if __name__ == "__main__":
    print("hello")
    print(get_todos())
