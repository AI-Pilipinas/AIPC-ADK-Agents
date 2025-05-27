import json

def update_todo(id: int, title: str, description: str) -> dict:
  """
  This tool updates a todo in the todo list.
  It takes in an id, title, and description and updates the todo in the list.
  It returns a message indicating that the todo was updated.
  """
  with open("todo_list/data/todos.json", "r") as f:
    todos = json.load(f)
  
  # Find the todo with the matching ID
  for i, todo in enumerate(todos["todos"]):
    if todo["id"] == id:
      todos["todos"][i] = {
        "id": id,
        "title": title,
        "description": description,
        "completed": False
      }
      with open("todo_list/data/todos.json", "w") as f:
        json.dump(todos, f)
      return {"message": f"Todo updated: {title}", "status": "success"}
  
  return {"message": f"Todo with ID {id} not found", "status": "error"}