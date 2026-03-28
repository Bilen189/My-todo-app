import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo_added = st.session_state["new_todo"].strip()
    if todo_added:  # avoid empty inputs
        todos.append(todo_added + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

st.title("My To-Do App")
st.subheader("")
st.write("")

for index, todo in enumerate(todos):
    if st.checkbox(todo, key=index):
        new_todos = todos.copy()
        new_todos.pop(index)
        functions.write_todos(new_todos)
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

