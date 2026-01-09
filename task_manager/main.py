import json
TASKS_FILE = "tasks.json"
def load_tasks():#تحميل المهام
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)#تقراها تحولها لقائمة
    except FileNotFoundError:
        return []#بدل متكسر البرنامج بترجع قائمة فاضي
def save_tasks(tasks):#حفظ المهام
    with open(TASKS_FILE, "w") as file:#كتابة المهام والمكتوب القديم يتم حدفه
        json.dump(tasks, file, indent=4)#يحول القائمة الى json
def add_task(tasks):
    title = input("Enter task title: ")
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully")
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✔" if task["completed"] else "❌"
        print(f'{task["id"]}. {task["title"]} [{status}]')
def complete_task(tasks):
    task_id = int(input("Enter task ID to complete: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("🎉 Task marked as completed")
            return
    print("Task not found.")
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("🗑️ Task deleted")
            return
    print("Task not found.")
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Man ager ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
