# import necessary functions
pick_bin=[]

# a function to help add an item to a pick bin
def add_item():
#    clear_output()
    item = input("What will you like to add?: ").title()
    pick_bin.append(item)
    print("{} as been added to the pick_bin".format(item))

# a function to remove an item from a pick_bin 
def remove_item():
#    clear_output()
    item = input("What would like to remove?: ").title()
    try:
        pick_bin.remove(item)
        print("{} has been remove".format(item))
    except:
        print("sorry we could not find that item")

# a function to show/view the items in the pick_bin
def view_pick_bin():
#   clear_output
    if pick_bin:
        print("Here is your pick_bin_items: ")
        for item in pick_bin:
            print("{}".format(item))
        else:
            print("your pick_bin is empty.")

#function to clear out all items from pick_bin
def clear_pick_bin():
#    clear_output()
    pick_bin.clear()
    print("Your pick_bin is empty.")

# MAIN PROGRAM
def main():
    finish = 0
    while not finish:
        enter = input("end/add/remove/view/clear: ").lower()

        if enter == "end":
            print("Thanks for using our program")
            
            view_pick_bin()
            finish = 1
        elif enter == "add":
           add_item()
        elif enter == "remove":
            view_pick_bin()
            remove_item
        elif enter == "view":
            view_pick_bin()
        elif enter == "clear":
            clear_pick_bin()
        else:
            print("sorry that is not an option")
main()
            
            
            
        
    
