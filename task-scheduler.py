rows, cols = (5, 8)
week = [[{"taskName": "", "taskDuration": 0, "populated": False, "startingHour":-1} for i in range(cols)] for j in range(rows)]

def print_week_schedule():
    d = 1
    for day in week:
        print(f"day {d}:")
        d += 1
        i = 9
        for hour in day:
            if hour["populated"] and hour["startingHour"] == i:
                print(f'task name: {hour["taskName"]}, start: {i}, end: {i + hour["taskDuration"]}')
            i += 1

def find_available_time(taskDuration):
    for day in range(len(week)):
        for startingHour in range(8):
            if startingHour + taskDuration > 7: continue
            existing_tasks_list = check_specific_time(week[day], startingHour, taskDuration)
            if not existing_tasks_list:
                return day, startingHour

def set_task(taskName, taskDuration, day, startingHour):
    for i in range(taskDuration):
        day[startingHour + i]["taskName"] = taskName
        day[startingHour + i]["taskDuration"] = taskDuration
        day[startingHour + i]["populated"] = True
        day[startingHour + i]["startingHour"] = startingHour + 9

def remove_task(i,j):
    startingHour = week[i][j]["startingHour"]
    for j in range(week[i][startingHour]["taskDuration"]):
        week[i][startingHour + j]["populated"] = False

def check_specific_time(day, startingHour, taskDuration):
    populated_hours = []
    for i in range(taskDuration):
        if day[startingHour + i]["populated"]:
            populated_hours.append(i)
    return populated_hours

def add_task(taskName, taskDuration, day = -1, startingHour = -1):
    if day == -1:
        day, startingHour = find_available_time(taskDuration)
        set_task(taskName, taskDuration, week[day], startingHour)
        print("The task was populated.")
    else:
        if startingHour + taskDuration > 7: 
            print("illegal!, can't work extra hours.")
            return
        existing_tasks_list = check_specific_time(week[day], startingHour, taskDuration)
        if not existing_tasks_list:
            set_task(taskName, taskDuration, week[day], startingHour)
        else:
            print("populated time, do you want to overwrite these tasks?:")
            for j in existing_tasks_list:
                print(week[day][j]["taskName"])
            if "yes" == input("yes/no?"):
                for j in existing_tasks_list:
                    remove_task(day,j)
                set_task(taskName, taskDuration, week[day], startingHour)
                print("The task was populated.")
            else:
                new_day = int(input("enter day:"))
                new_startHour = int(input("enter hour:"))
                add_task(taskName, taskDuration, new_day, new_startHour)

while True:
    if input("do you want to add tasks? yes/no?") == "yes":
        task_name = input("enter task name:")
        task_duration = int(input("enter task duration:"))
        if input("do you have specefic time? yes/no?") == "yes":
            task_day = int(input("enter task day:"))
            task_starting_hour = int(input("enter task starting hour:"))
            add_task(task_name, task_duration, task_day, task_starting_hour)
        else:
            add_task(task_name, task_duration)
    else:
        break

print_week_schedule()