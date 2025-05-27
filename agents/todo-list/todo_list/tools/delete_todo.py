import json

def delete_todo(id: int) -> dict:
  """
  This tool deletes a todo from the todo list.
  It takes in an id and deletes the todo from the list.
  It returns a message indicating that the todo was deleted.
  """
  with open("todo_list/data/todos.json", "r") as f:
    todos = json.load(f)
  todos["todos"] = [todo for todo in todos["todos"] if todo["id"] != id] 
  with open("todo_list/data/todos.json", "w") as f:
    json.dump(todos, f)
  return {"message": f"Todo deleted: {id}", "status": "success"}