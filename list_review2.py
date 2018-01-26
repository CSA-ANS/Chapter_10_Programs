#Ammaar Siddiqui
#Comp Prog
#1/22/2018
import random
def list_function():
    myList=[]
    myList.append(76)
    myList=myList+[92.3]
    myList.append("hello")
    myList=myList+[True]
    myList.append(4)
    myList=myList+[76]
    print(myList)

def random_numbers():
    numbers=[]
    for x in range(100):
        number=random.randrange(1,1001)
        numbers.append(number)
    print(average_numbers(numbers))
        
def average_numbers(numbers):
    listSum=sum(numbers)
    listLen=len(numbers)
    listAverage=listSum/listLen
    return(listAverage)

list_function()
random_numbers()
