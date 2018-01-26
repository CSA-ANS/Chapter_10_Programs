#Ammaar Siddiqui
#Comp Prog
#1/24/2018
def make_list():#starts of program by making original list
    names=["Zach","Greg","Jacob","Denver","Ammaar"]
    add_name(names)#starts the add name function
    print(print_names(names))#prints whatever is returned
def add_name(names):#add name finction
    add=input("What name would you like to add: ")
    names.append(add)#asks what name they would like to add and adds it 
    menu(names)#goes to the menu function
def menu(names):#wether they would like to add a nother name
    print("1. Yes")
    print("2. No")
    choice=input("Would you like to add another name? ")#asks them wether they would like to add another name or not
    if choice=="1":
        add_name(names)#goes back to add name function if they say yes
    elif choice=="2":#goes to return function if they say no
        print_names(names)#runs return function and passes it the value
    else:
        print("Invalid Choice")#goes back to the beginning of the menu if they enter in wrong
        menu(names)
def print_names(names):
    return names#returns name which can be printed by the first function
make_list()
    
