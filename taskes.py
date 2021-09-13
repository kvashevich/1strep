menu = """
1. Show task
2. Add task
3. Edit task
4. Delete task
5. Erase task
6. EXit\n """

taskes = []


def check():
    return print(*taskes)


def add():
    vvod = input('What do you want to do?')
    count = len(taskes)
    taskes.append(f"{count + 1}.{vvod}")
    return print('task adds')


def edit():
    vvod = input('which task to edit?')
    task = [task for task in taskes if task.startswith(vvod)][0]
    index_task = taskes.index(task)
    etask = input("new name: ")
    taskes[index_task] = f"{task.split('.')[0]}.{etask}"
    return print('task edited')


def delete():
    delet = input('which task to delete?')
    task = [task for task in taskes if task.startswith(delet)][0]
    index_task = taskes.index(task)
    taskes.pop(index_task)
    return print('Task deleted')


def erase():
    vvod = input('which task is done?')
    task = [task for task in taskes if task.startswith(vvod)][0]
    index_task = taskes.index(task)
    taskes[index_task] = f"{task} (done)"
    return print('task complited')


menu_list = {
    '1': check,
    '2': add,
    '3': edit,
    '4': delete,
    '5': erase,
}

while True:
    print(menu)
    ent = input()
    if ent == "6":
        print('end.')
        break
    menu_list[ent]()
