class to_do:
    def __init__(self):
        self.tasks = {}
    
    def user_int(self):
        pass
    def add_task(self, task, due_date):
        self.tasks[task] = due_date

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
    def show_task(self):
        for task, due_date in self.tasks.items():
            print(f"Task: {task} Due: {due_date}")