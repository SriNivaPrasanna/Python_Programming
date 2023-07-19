from todo_helper import create_table, add_todo, read_todos, update_todo, delete_task, close_connection

def main():
    run = 1

    while run:
        create_table()
        print("Press 1: To add todo")
        print("Press 2: To read todos")
        print("Press 3: To update todo")
        print("Press 4: To delete todo")
        print("Press 5: To Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            todo = input("enter todo to be added: ")
            add_todo(todo)
        elif ch == "2":
            read_todos()
        elif ch == "3":
            idx = int(input("Enter the id of todo to be updated"))
            updated_todo = input("enter updated todo: ")
            update_todo(idx, updated_todo)
        elif ch == "4":
            idx = int(input("Enter the id of todo to be updated"))
            delete_task(idx)
        elif ch == "5":
            run = 0

    close_connection()


if __name__ == '__main__':
    main()