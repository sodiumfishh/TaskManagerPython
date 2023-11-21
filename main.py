class Task:
    def __init__(
        self, title, description=None, deadline=None, isCompleted=False, steps=[]
    ):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.isCompleted = isCompleted
        self.steps = Stack(steps)  # Initialize the steps as a Stack


class Step:
    def __init__(self, description, isCompleted=False):
        self.description = description
        self.isCompleted = isCompleted


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data


class Stack:
    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]


def main():
    task_queue = Queue()

    while True:
        print("\n1. Add a task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task(task_queue)
        elif choice == 2:
            view_all_tasks(task_queue)
        elif choice == 3:
            delete_task(task_queue)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")


def add_task(task_queue):
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    deadline = input("Enter the deadline of the task: ")

    task = Task(title, description, deadline)

    add_steps = input("Do you want to add steps to the task? (yes/no): ")

    if add_steps.lower() == "yes":
        num_steps = int(input("Enter the number of steps: "))
        steps_stack = Stack()

        for i in range(num_steps):
            step_description = input(f"Enter the description of step {i+1}: ")
            step = Step(step_description)
            steps_stack.push(step)

        task.steps = steps_stack

    task_queue.enqueue(task)


def view_all_tasks(task_queue):
    current = task_queue.front
    while current:
        task = current.data
        print(
            f"Title: {task.title}, Description: {task.description}, Deadline: {task.deadline}"
        )
        current = current.next


def delete_task(task_queue):
    title = input("Enter the title of the task to delete: ")
    current = task_queue.front
    prev = None

    while current:
        if current.data.title == title:
            if prev:
                prev.next = current.next
            else:
                task_queue.front = current.next
            return
        prev = current
        current = current.next

    print("Task not found.")


if __name__ == "__main__":
    main()
