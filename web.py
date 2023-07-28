import streamlit as st
import functions


todos = functions.get_todos()
print(todos)


def add_todo():
    global todos
    todo_new = st.session_state['new_todo'].title() + "\n"
    if not todo_new == "\n":
        todos.append(todo_new)
        functions.write_todos(todos)


def complete_todo():
    global todos
    pass


st.title("My Todo App")
st.subheader("This is my todo app. ")
st.write("This app will increase your productivity")

# st.checkbox("todo item #1")


for index, todo in enumerate(todos):
    if todo == "\n":
        todos.pop(index)

    else:
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()


st.text_input(label="Enter a todo: ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


st.session_state
