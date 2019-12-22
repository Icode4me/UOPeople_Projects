"""

This is a Todo list that will ask you if you want to add a task to the todo list
then display the list at the end of all the tasks you've added
this is basic and can be enhanced feel free to fork
I will also be making changes to it

"""

# First let's create an empty list object
todo = []

# we next will ask if user wants to add and item and give option to user yes or no
# if no programs dies
# if yes then will be asked to enter the task to add to the list
# and will repeat while your answer is no

add = input('would you like to add a task to your todo list? Yes or No...:   ')
while add == 'yes' or add == 'Yes':
    todo.append(input("enter an item to add to the todo list ...:  "))
    add = input(
        'would you like to add another task to your todo list? Yes or No...:   ')
    if add == 'no' or add == 'No':
        print(todo)
        break
    else:
        todo.append(
            input('Add another task to do list ... :   '))
        q = input('Would you like to add another task? Yes or No ? ... :   ')
        if q == 'yes' or 'Yes':
            todo.append(input("enter an item to add to the todo list ...:  "))
        else:
            print(todo)
            break
            
# print the todo list each item per line
for i in todo:
    print(i)
