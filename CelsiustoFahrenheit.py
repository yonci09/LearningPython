# by using the formula F = 1.8 * C + 32 
# convert from degrees Celsius to degrees Fahrenheit


# getting the value for C and converting it to integer
deg_cel = int(input("Please enter an integer value for degrees celsius. "))
 
#creating a function which calculates the C-F
def Fahrenheit(cel):
    #to get rid of decimal point all numbers are multiplied by 10 then divided bt 10.
    return (18 * cel + 320) / 10
 
 
print("The Fahrenheit equivalent of " + str(deg_cel) + " degrees Celsius is " + str(Fahrenheit(deg_cel)) + ".")