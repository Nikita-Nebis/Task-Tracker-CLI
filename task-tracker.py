import argparse
import json
import os
from datetime import datetime

DB_FILE = "tasks.json"

def get_now() -> str:
    # Format: DD-MM HH:MM:SS
    return datetime.now().strftime("%d-%m %H:%M:%S")

def load_tasks() -> list:
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks) -> None:
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

# --- Command Logic ---

def add_task(args) -> None:
    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    now = get_now()
    new_task = {
        "id": new_id,
        "title": args.title,
        "status": "pending",
        "created_at": now,
        "updated_at": now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added: [ID {new_id}] {args.title}")

def update_task(args) -> None:
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == args.id:
            if args.title: t["title"] = args.title
            if args.status: t["status"] = args.status
            if args.title or args.status:
                t["updated_at"] = get_now()
            save_tasks(tasks)
            print(f"Task {args.id} updated successfully.")
            return
    print(f"Error: Task with ID {args.id} not found.")

def delete_task(args) -> None:
    tasks = load_tasks()
    initial_count = len(tasks)
    tasks = [t for t in tasks if t["id"] != args.id]
    if len(tasks) < initial_count:
        save_tasks(tasks)
        print(f"Task {args.id} deleted.")
    else:
        print(f"Error: Task with ID {args.id} not found.")

def list_tasks(args) -> None:
    tasks = load_tasks()
    if not tasks:
        print("Task list is empty.")
        return
    print(f"{'ID':<3} | {'Status':<8} | {'Task Title':<25} | {'Created':<15} | {'Updated':<15}")
    print("-" * 77)
    for t in tasks:
        # Using checkmark for done and X for pending
        status_icon = "✔" if t["status"] == "done" else "✘"
        print(f"{t['id']:<3} | {status_icon:<8} | {t['title']:<25} | {t['created_at']:<15} | {t['updated_at']:<15}")

# --- Argparse Configuration ---

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # ADD
    add_p = subparsers.add_parser("add", help="Add a new task")
    add_p.add_argument("title", help="Title of the task")
    add_p.set_defaults(func=add_task)

    # LIST
    list_p = subparsers.add_parser("list", help="Show all tasks (Time format: DD-MM HH:MM:SS)")
    list_p.set_defaults(func=list_tasks)

    # DELETE
    del_p = subparsers.add_parser("delete", help="Delete a task by ID")
    del_p.add_argument("id", type=int, help="The ID of the task to delete")
    del_p.set_defaults(func=delete_task)

    # UPDATE
    upd_p = subparsers.add_parser("update", help="Update an existing task")
    upd_p.add_argument("id", type=int, help="The ID of the task to update")
    upd_p.add_argument("-t", "--title", help="New title for the task")
    upd_p.add_argument("-s", "--status", choices=["pending", "done"], help="New status (pending/done)")
    upd_p.set_defaults(func=update_task)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()