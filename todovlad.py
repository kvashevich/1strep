todos = []


def strike(text):
    result = ''
    for c in text:
        result += c + '\u0336'
    return result


def strike_todo(todo):
    return strike(todo["text"]) if todo["is_done"] else todo["text"]


def valid_todo_number(number):
    return number.isdigit() and 0 < int(number) <= len(todos)


def yes_no_todo_choice(number, todo, action):
    print(f'Todo {number}. {todo["text"]} {action} succes!')
    y = input(f'Do you want to {action} another one? (y/n) ')
    return y in ('y', 'Y')


def add_todo(text):
    todo = {
        "text": text,
        "is_done": False
    }
    todos.append(todo)
    return todo


def update_todo_text(number, text):
    todo = todos[number]
    todo["text"] = text
    return todo


def delete_todo(number):
    todo = todos.pop(number)
    return todo


def update_todo_is_done(number):
    todo = todos[number]
    todo["is_done"] = not todo["is_done"]
    return todo


def print_todos():
    # for i, todo in enumerate(todos):
    i = 1
    print('Todo list:')
    for todo in todos:
        print(f'{i}. {strike_todo(todo)}')
        i += 1
    return True


def print_add_todos():
    while True:
        print_todos()
        text = input('Enter new todo - ')
        todo = add_todo(text)
        if not yes_no_todo_choice(len(todos), todo, 'add'):
            break
    return True


def print_delete_todos():
    while len(todos):
        print_todos()
        number = input('Enter valid todo number you want to delete - ')
        if not valid_todo_number(number):
            print('Non valid todo number!\n')
            print_todos()
            continue
        number = int(number)
        todo = delete_todo(number - 1)
        if not yes_no_todo_choice(number, todo, 'delete'):
            break
    else:
        print('There are no todos')
    return True


def print_update_todos_text():
    while True:
        print_todos()
        number = input('Enter valid todo number you want to update - ')
        if not valid_todo_number(number):
            print('Non valid todo number!\n')
            print_todos()
            continue
        number = int(number)
        text = input('Enter text you want update to - ')
        todo = update_todo_text(number - 1, text)
        if not yes_no_todo_choice(number, todo, 'delete'):
            break
    return True


def print_update_todos_is_done():
    while True:
        print_todos()
        number = input('Enter valid todo number you want to mark - ')
        if not valid_todo_number(number):
            print('Non valid todo number!\n')
            print_todos()
            continue
        number = int(number)
        todo = update_todo_is_done(number - 1)
        if not yes_no_todo_choice(number, todo, 'mark'):
            break
    return True


def todos_exit():
    y = input('Are you sure? You data will not be saved! (y/n) ')
    if y in ('y', 'Y'):
        print('Have a nice day! Bye!')
        exit()


choices = {
    "1": print_todos,
    "2": print_add_todos,
    "3": print_update_todos_text,
    "4": print_update_todos_is_done,
    "5": print_delete_todos,
    "0": todos_exit
}

menu = """
Choice menu option:\n
1. Show todo list
2. Add new todo
3. Update todo
4. Mark todo as done/undone
5. Delete todo
0. Exit\n
"""

while True:
    menu_number = input(menu)
    choice = choices.get(menu_number)
    if not choice:
        print('Non valid menu option')
        continue
    choice()

