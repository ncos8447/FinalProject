import json
import os

FILE_NAME = "tasks.txt"

#load tasks from the file

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    tasks = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                task = json.loads(line)
                tasks.append(task)
    return tasks

#save tasks to file

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            json_string = json.dumps(task)
            file.write(json_string + "\n")

