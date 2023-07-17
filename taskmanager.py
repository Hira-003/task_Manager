from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["task_manager"]
collection = db["tasks"]

def add_task():
    task = input("Enter a task: ")
    collection.insert_one({"task": task})
    print("Task added successfully!")

def view_tasks():
    count = collection.count_documents({})
    if count == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        tasks = collection.find({})
        for task in tasks:
            print(task["task"])

def remove_task():
    tasks = list(collection.find())
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        view_tasks()
        choice = int(input("Enter the task number to remove: "))
        if choice < 1 or choice > len(tasks):
            print("Invalid task number.")
        else:
            task = tasks[choice - 1]
            collection.delete_one({"_id": task["_id"]})
            print(f"Task '{task['task']}' removed successfully!")

# Rest of the code remains the same
# ...

def menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

while True:
    menu()
    option = input("Enter your choice (1-4): ")
    if option == "1":
        add_task()
    elif option == "2":
        view_tasks()
    elif option == "3":
        remove_task()
    elif option == "4":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
