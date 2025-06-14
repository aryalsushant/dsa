"""

"""

def get_highest_priority_task(tasks):
    highest_priority = 0
    best_task = ""
    for task, priority in tasks.items():
        if priority > highest_priority:
            highest_priority = priority
            best_task = task
    tasks.pop(best_task)
    return best_task

#test case
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)





