import todofunc
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
while True:
    user_prompt = input("Type add,show,complete,edit or exit:")
    user_prompt = user_prompt.strip()
    if user_prompt.startswith('add'):
            todo = user_prompt[4:]
            todos = todofunc.get_todos()
            todos.append(todo)
            todofunc.write_todos(todos,"todos.txt")

    elif user_prompt.startswith('show'):
            todos = todofunc.get_todos()
            New_todo = []
            for index, items in enumerate(todos):
                items = items.strip('\n')
                row = f"{index + 1} - {items}"
                print(row)
    elif user_prompt.startswith('edit'):
            try:
                num = int(user_prompt[5:])
                num = num-1
                todos = todofunc.get_todos()
                new_todo=input("Enter a new todo: ")
                todos[num]=new_todo+'\n'
                todofunc.write_todos(todos_arg=todos)
            except ValueError:
                print("Invalid command")
            continue

    elif user_prompt.startswith('complete'):
           try:
                num = int(user_prompt[9:])
                todos = todofunc.get_todos()
                ind = num-1
                word_to_removed = todos[ind]
                todos.pop(ind)
                todofunc.write_todos(todos_arg=todos)
                print(f'The todo that was completed is {word_to_removed}')
           except IndexError:
               print("Index out of range")
    elif user_prompt.startswith('exit'):
            break
    else:
            print("HEy, you entered an unknown command")

print("Bye!")