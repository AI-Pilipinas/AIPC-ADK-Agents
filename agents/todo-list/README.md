# Todo List Agent

A simple and efficient todo list management agent built with the Google Agent Development Kit (ADK). This agent helps you manage your tasks by providing functionality to add, update, delete, and track your todos.

## Features

- **Add Todos**: Create new tasks with titles and descriptions
- **Update Todos**: Modify existing tasks
- **Delete Todos**: Remove tasks you no longer need
- **View Todos**: List all your current tasks
- **Complete Todos**: Mark tasks as completed

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Virtual environment management tool (venv, conda, etc.)
- Google ADK installed (`pip install google-adk`)

### Setting Up Your Environment

1. Create and activate a virtual environment:

   **Using venv (recommended):**

   ```bash
   # Create a virtual environment
   python -m venv .venv

   # Activate the virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. Install the Google ADK:
   ```bash
   pip install google-adk
   ```

### Running the Agent

1. Navigate to the todo-list agent directory:

   ```bash
   cd agents/todo-list
   ```

2. Run the agent:
   ```bash
   adk web
   ```

## Usage Examples

The agent supports the following commands:

- Add a new todo:

  ```
  Add a todo: "Buy groceries" with description "Get milk, eggs, and bread"
  ```

- Update a todo:

  ```
  Update todo 1 with title "Buy groceries" and description "Get milk, eggs, bread, and cheese"
  ```

- Delete a todo:

  ```
  Delete todo 1
  ```

- View all todos:

  ```
  Show me all todos
  ```

- Complete a todo:
  ```
  Mark todo 1 as completed
  ```

## Directory Structure

```
todo-list/
├── todo_list/                    # Core Agent Code
│   ├── tools/                    # Contains the code for tools
│   │   ├── add_todo.py          # Tool for adding todos
│   │   ├── delete_todo.py       # Tool for deleting todos
│   │   ├── get_todos.py         # Tool for retrieving todos
│   │   ├── update_todo.py       # Tool for updating todos
│   │   └── complete_todo.py     # Tool for marking todos as complete
│   ├── __init__.py              # Initializes the agent
│   ├── agent.py                 # Contains the core logic of the agent
│   └── prompt.py                # Contains the prompts for the agent
├── data/                        # Data storage
│   └── todos.json              # JSON file storing todos
└── README.md                    # This file
```

## Data Storage

The agent stores todos in a JSON file located at `todo_list/data/todos.json`. The structure of the JSON file is:

```json
{
  "todos": [
    {
      "id": 1,
      "title": "Example Todo",
      "description": "This is an example todo",
      "completed": false
    }
  ]
}
```

## Contributing

Feel free to contribute to this project by:

1. Reporting bugs
2. Suggesting new features
3. Submitting pull requests

## License

This project is licensed under the same terms as the Google ADK.
