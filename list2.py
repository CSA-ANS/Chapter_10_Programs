def print_info():
    info=["Ammaar Siddiqui",26,"March",2003,"Austin"]
    index=0
    for x in range(5):
        print(info[index])
        index+=1
    print("I was born in "+info[4]+".")
    print("The month was "+info[2]+".")
    info[1:1]=["Najam"]
    print(info)

print_info()
