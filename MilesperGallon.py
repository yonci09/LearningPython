#create a program that approximates the number of miles per gallon that a car can get.
#create two variables, one which will hold a randomly generated integer between 10 and 25 (inclusive of both 10 and 25), 
#and another which will hold a randomly generated integer between and inclusive of 200 and 400.
#The first variable represents the number of gallons of gas that the car's fuel tank holds. The second variable represents the miles that the car can travel on a full tank before needing a refuel.
# miles per gallon (MPG) = miles driven/gallons used, 
#calculate the car's MPG and display it in the output using print(). 


from random import randint

#randomly generated integers
car_fuel = randint(10, 25)
car_miles = randint(200, 400)


#calucalating
gallon = car_miles/car_fuel

#printing result
print(int(gallon))

print(str(car_miles))

print(str(car_fuel))


