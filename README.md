# 📝 Task Tracker CLI

A lightweight and efficient Task Management tool for your terminal. Built with Python, this tool helps you stay organized using a simple command-line interface and local JSON storage.

## ✨ Key Features

* **Zero Dependencies:** Uses only Python standard libraries (`argparse`, `json`, `datetime`).
* **Persistent Storage:** Data is safely stored in a local `tasks.json` file.
* **Automated Timestamps:** Tracks exactly when a task was `Created` and last `Updated`.
* **Intuitive Interface:** Structured sub-commands with built-in validation.

## 🛠 Usage

The script is invoked via the terminal using specific commands.

### Commands Overview

| Command  | Description                      | Example                                |
| :------- | :------------------------------- | :------------------------------------- |
| `add`    | Create a new task                | `python tasks.py add "Buy groceries"`  |
| `list`   | Display all tasks with details   | `python tasks.py list`                 |
| `update` | Modify title or status           | `python tasks.py update 1 -s done`     |
| `delete` | Remove a task by ID              | `python tasks.py delete 1`             |

### Detailed Examples

**Adding a Task:**
```bash
python tasks.py add "Finish the Python project"
