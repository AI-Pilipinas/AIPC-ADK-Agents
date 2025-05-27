import json

def complete_todo(id: int) -> dict:
  """
  This tool completes a todo in the todo list.
  It takes in an id and completes the todo in the list.
  It returns a message indicating that the todo was completed.
  """
  with open("todo_list/data/todos.json", "r") as f:
    todos = json.load(f)
  todos["todos"][id - 1]["completed"] = True
  with open("todo_list/data/todos.json", "w") as f:
    json.dump(todos, f)
  return {"message": f"Todo completed: {id}", "status": "success"}