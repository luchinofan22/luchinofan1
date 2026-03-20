#Build a program that simulates a to-do list with saving/loading
to_do_list = []
initial_list = input("Please type your To-Do list: ")
initial_list.split(",")
to_do_list.append(initial_list)
print(to_do_list)
def save_list(your_list_here):
    return to_do_list == your_list_here

def add_item(list_b):
    item = input("What item would you like to add to your to-do list?")
    list_b.append(item)
    save_list(list_b)
    return list_b
