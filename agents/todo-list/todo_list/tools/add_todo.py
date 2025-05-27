import json

def add_todo(title: str, description: str) -> dict:
  """
  This tool adds a todo to the todo list.
  It takes in a title and description and adds a new todo to the list.
  It returns a message indicating that the todo was added.
  """
  with open("todo_list/data/todos.json", "r") as f:
    todos = json.load(f)
  todos["todos"].append({
    "id": todos["todos"][-1]["id"] + 1,
    "title": title,
    "description": description,
    "completed": False
  })
  with open("todo_list/data/todos.json", "w") as f:
    json.dump(todos, f)
  return {"message": f"Todo added: {title}", "status": "success"}