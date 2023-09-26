# writing a program which uses a for loop to reverse a string. 



your_string = input("Could you please enter a string: ")
reversed_string = ""
 
for item in range(len(your_string) - 1, -1, -1):
    reversed_string += your_string[item]
 
print(reversed_string)



