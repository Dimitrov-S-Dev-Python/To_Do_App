import functions
import time

now = time.strftime("%b %d, %Y %H:%M")
print(f"{now}")
while True:
	user_action = input("Type add, show, edit, remove  or exit:\n-> ")
	user_action = user_action.strip()
	if user_action.startswith("add"):
		todo = user_action[4:]

		todos = functions.get_todos()

		todos.append(todo + '\n')

		functions.write_todos(todos)

	elif user_action.startswith("show"):
		todos = functions.get_todos()
		for index, item in enumerate(todos):
			item = item.strip("\n")
			row = f"{index + 1}-{item}"
			print(row)
	elif user_action.startswith("edit"):
		try:
			number = int(user_action[5:])
			number -= 1

			todos = functions.get_todos()

			new_todo = input("Enter new todo: ")
			todos[number] = new_todo + "\n"

			functions.write_todos(todos)
		except ValueError:
			print(f"Your command is not valid!")
			continue

	elif user_action.startswith("remove"):
		try:
			number = int(user_action[7:])

			todos = functions.get_todos()
			index = number - 1
			remove = todos[index].strip("\n")
			todos.pop(index)

			functions.write_todos(todos)
			print(f"{remove} was removed from list!")
		except IndexError:
			print("There is no item with such a number!")
			continue
	elif user_action.startswith("exit"):
		print("Bye!")
		break
	else:
		print("Hey, you enter an unknown command")
