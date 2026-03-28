import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo_added = st.session_state["new_todo"].strip()

    if todo_added:
        clean_todos = [t.strip() for t in todos]

        if todo_added in clean_todos:
            st.warning("⚠️ This todo already exists!")
        else:
            todos.append(todo_added + "\n")
            functions.write_todos(todos)
            st.session_state["new_todo"] = ""

st.title("My To-Do App")
st.subheader("")
st.write("Use your To-Do app to control your tasks and be <b>more productive.</b>",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
for index, todo in enumerate(todos):
    key = f"{todo}_{index}"

    if st.checkbox(todo.strip(), key=key):
        new_todos = todos.copy()
        new_todos.pop(index)
        functions.write_todos(new_todos)
        del st.session_state[key]
        st.rerun()



