#Create a dictionary and take input from the user and return the meaning of the

# word from the dictionary

dict = {"mutable":"can be change",
        "immutable":"can not be change",
        "abundant":"exist in large quantity"}
#key = input("Word:")
#print("Meaning:",dict[key])



print("Enter the Following keys to know the meaning:")
print("  mutable  \n  immutable  \n  abundant")
user_input=input("Enter the above keys:")
print("meaning:",dict[user_input])