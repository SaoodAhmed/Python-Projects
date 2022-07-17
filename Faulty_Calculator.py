#Design a calculator which will correctly solve all the problems except
#the following ones:
#45 * 3 = 55, 56 + 9=77, 56\6=4
#your program should take the operator and two numbers as input from the user
#and then  return the result

#Faulty Calculator

print("Enter the operator:")
oprt = input()
print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())
if num1==56 and num2==9 and oprt=='+':
     print("Addition is: 77")
elif oprt=='+':
    print("Addition is:",num1+num2)
elif num1==45 and num2==3 and oprt=='*':
    print("Multiplication is: 55")
elif oprt=='*':
    print("Multiplication is:",num1*num2)
elif num1==56 and num2==6 and oprt=='/':
    print("Division is: 4")
elif oprt=='/':
    print("Division is:",num1/num2)
else:
    print("subtraction is :", num1 - num2)