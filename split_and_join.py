#Ammaar Siddiqui
#Comp Prog
#1/25/2018

def split():#splits 2 strings into lists
    string1="My name is Jose"#defines first string
    list1=string1.split()#splits it by default using the spaces
    print(list1)#prints the splitted string
    string2="user1;user2;user3"#defines second string
    list2=string2.split(";")#splits it using a ; as the parameter
    print(list2)#prints splitted string without semicolons

def join():#joins alist into a string
    list1=["this","is","a","sentence"]#defines string
    glue=" "#what will be in the middle when it is combined
    string1=glue.join(list1)#Joins the list with spaces
    print(string1)#prints the combined list
    

split()#runs first function
join()#runs second function
