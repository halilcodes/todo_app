FILEPATH = "todo_list.txt"


def show_list(todo_list):
    print(todo_list)
    for num, do in enumerate(todo_list):
        print(f"{num}- {do.title()}", end="")
    print()


def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r+", encoding="utf8") as f:
            my_list = f.readlines()
            if not my_list[-1].endswith("\n"):
                my_list[-1] += "\n"
            return my_list
    except FileNotFoundError:
        with open(filepath, "w", encoding="utf8") as _:  # create the file if not exists.
            return []


def write_todos(todo_list, filepath=FILEPATH):
    with open(FILEPATH, "w", encoding="utf8") as file:
        file.writelines(todo_list)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
