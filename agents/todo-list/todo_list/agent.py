"""A todo list agent that can add, remove, and view todos. It can also update and complete todos."""

from google.adk.agents import Agent

from .tools import (
    add_todo,
    delete_todo,
    get_todos,
    update_todo,
    complete_todo
)
from .prompt import todo_list_prompt

root_agent = Agent(
  name="todo_list_agent",
  model="gemini-2.0-flash",
  description="A todo list agent that can add, remove, and view todos.",
  instruction=todo_list_prompt,
  tools=[
    add_todo,
    delete_todo,
    get_todos,
    update_todo,
    complete_todo
  ]
)
