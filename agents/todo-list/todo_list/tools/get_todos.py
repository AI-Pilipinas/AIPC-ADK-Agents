import json

def get_todos() -> dict:
  """
  This tool gets all the todos from the todo list.
  It returns a list of todos.
  """
  with open("todo_list/data/todos.json", "r") as f:
    todos = json.load(f)
  return {
    "todos": todos["todos"],
    "status": "success"
  }