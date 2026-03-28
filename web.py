import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo_added = st.session_state["new_todo"].strip()

    if todo_added:
        if todo_added + "\n" in todos:
            st.warning("⚠️ This todo already exists!")
        else:
            todos.append(todo_added + "\n")
            functions.write_todos(todos)
            st.session_state["new_todo"] = ""

st.title("My To-Do App")
st.subheader("")
st.write("Your To-Do app allows you to manage your tasks and be <b>productive daily</b>.",
         unsafe_allow_html=True)
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
st.set_page_config(layout="wide")
for index, todo in enumerate(todos):
    if st.checkbox(todo, key=todo):
        new_todos = todos.copy()
        new_todos.pop(index)
        functions.write_todos(new_todos)
        del st.session_state[todo]
        st.rerun()



