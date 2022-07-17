
# total 6 files

# Write a function that when executed takes as input client name
# step 1 lock or retreive
# step 2 name of client
# step 3 lock excercise or diet
# step 4 done
# ******NOTE : all detail are saved in only file,.
# this is just for testing , we can also create separate file for each user**



def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            value = input("Type here\n")
            with open("Saud-exe.txt","a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("sucessfully written!!")
        elif c == 2:
             value = input("Type here\n")
             with open("Saud-food.txt","a") as op:
                 op.write(str([str(getdate())]) + ": " + value + "\n")
             print("sucessfully written!!")
    elif k==2:
         c = int(input("Enter 1 for exercise and 2 for food: "))
         if c == 1:
             value = input("Type here\n")
             with open("Farman-exe.txt","a") as op:
                 op.write(str([str(getdate())]) + ": " + value + "\n")
             print("sucessfully written!!")
         elif c == 2:
             value = input("Type here\n")
             with open("Farman-food.txt","a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
             print("sucessfully written!!")
    elif k == 3:
         c = int(input("Enter 1 for exercise and 2 for food: "))
         if c == 1:
             value = input("Type here\n")
             with open("Hamza-exe.txt","a") as op:
                 op.write(str([str(getdate())]) + ":" + value + "\n")
             print("sucessfully written!!")
         elif c == 2:
             value = input("type here\n")
             with open("Hamza-food.txt","a") as op:
                 op.write(str([str(getdate())]) + ":" + value + "\n")
             print("written sucessfully!!")
    else:
         print("plz enter a valid input 1-Saud, 2-Farman, 3-Hamza")

def retrieve(k):
    if k == 1:
        c = int(input("1 for exercise and 2 for food: "))
        if c == 1:
            with open("Saud-exe.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("saud-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k == 2:
        c = int(input("1 for exercise and 2 for food: "))
        if c == 1:
            with open("Farman-exe.txt") as op:
                for i in op:
                    print(i,end="")
        elif c == 2:
            with open("Farman-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k == 3:
        c = int(input("1 for exercise and 2 for food: "))
        if c == 1:
            with open("Hamza-exe.txt") as op:
                for i in op:
                    print(i,end="")
        if c == 2:
            with open("Hamza-food.txt") as op:
                for i in op:
                    print(i,end="")
    else:
        input("plz enter valid input (1-Saud, 2-Farman, 3-Hamza)")


print("****HEALTH MANAGEMENT SYSTEM****\n")
a = int(input("1 for log the value and 2 for retrieve the value: "))
if a == 1:
    b = int(input("Press 1 for Saud 2 for Farman and 3 for Hamza: "))
    take(b)
else:
    b = int(input("Press 1 for Saud 2 for Farman and 3 for Hamza: "))
    retrieve(b)