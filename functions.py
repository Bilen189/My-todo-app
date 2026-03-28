FILEPATH = "todos.txt"

def get_todos(filename = FILEPATH):
    """Read a text file and return the list of to-do items.
    """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todo_arg , filename = FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filename, "w") as file:
        file.writelines(todo_arg)


#__name__ is equal to __main__ when it is run with in this code.
# But when it is imported it will be equal to functions, which means __name__ == "functions"
# instead of __name__ == "__main__"so the program underneath only runs when someone
# runs it in this program but not when it is imported
if __name__ == "__main__":
    print("hello")
    print(get_todos())