import uuid
from models.person import Person
from models.user import User
from models.project import Project
from models.task import Task
from utils.io_manager import load_data, save_data

def generate_id():
    return str(uuid.uuid4())[:8]

def find_user(data, name):
    for user in data["users"]:
        if user["name"] == name:
            return user
    return None

def find_project(data, title):
    for project in data["projects"]:
        if project["title"] == title:
            return project
    return None

def add_user_menu():
    name = input("Enter name: ")
    email = input("Enter email: ")
    data = load_data()
    user = {"id": generate_id(), "name": name, "email": email}
    data["users"].append(user)
    save_data(data)
    print(f"User '{name}' added successfully.")

def list_users_menu():
    data = load_data()
    if not data["users"]:
        print("No users found.")
        return
    for user in data["users"]:
        print(f"- {user['name']} ({user['email']})")

def add_project_menu():
    user_name = input("Enter user name: ")
    title = input("Enter project title: ")
    description = input("Enter project description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    data = load_data()
    user = find_user(data, user_name)
    if not user:
        print("User not found.")
        return
    project = {
        "id": generate_id(),
        "title": title,
        "description": description,
        "due_date": due_date,
        "owner_id": user["id"]
    }
    data["projects"].append(project)
    save_data(data)
    print(f"Project '{title}' added to {user_name}.")

def list_projects_menu():
    user_name = input("Enter user name: ")
    data = load_data()
    user = find_user(data, user_name)
    if not user:
        print("User not found.")
        return
    projects = [p for p in data["projects"] if p["owner_id"] == user["id"]]
    if not projects:
        print("No projects found.")
        return
    for p in projects:
        print(f"- {p['title']} (Due: {p['due_date']})")

def add_task_menu():
    project_title = input("Enter project title: ")
    task_title = input("Enter task title: ")
    data = load_data()
    project = find_project(data, project_title)
    if not project:
        print("Project not found.")
        return
    task = {
        "id": generate_id(),
        "title": task_title,
        "status": "Pending",
        "project_id": project["id"]
    }
    data["tasks"].append(task)
    save_data(data)
    print(f"Task '{task_title}' added to project '{project_title}'.")

def complete_task_menu():
    task_id = input("Enter task ID: ")
    data = load_data()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_data(data)
            print(f"Task '{task['title']}' marked as complete.")
            return
    print("Task not found.")

def main():
    while True:
        print("\n--- Project Tracker Menu ---")
        print("1. Add User")
        print("2. List Users")
        print("3. Add Project")
        print("4. List Projects")
        print("5. Add Task")
        print("6. Complete Task")
        print("7. Exit")
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            add_user_menu()
        elif choice == "2":
            list_users_menu()
        elif choice == "3":
            add_project_menu()
        elif choice == "4":
            list_projects_menu()
        elif choice == "5":
            add_task_menu()
        elif choice == "6":
            complete_task_menu()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
