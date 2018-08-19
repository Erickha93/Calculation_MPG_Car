#!/usr/bin/env python3
The Miles Per Gallon application

Enter trip distance:		500
Enter miles gallon:		50
Enter cost per gallon:		3.24

Miles Per Gallon:		 50.0
Miles Per Gallon:		 10.0
Miles Per Gallon:		 32.4

Continue (y/n)?: y

Enter trip distance:		325
Enter miles gallon:		18.50
Enter cost per gallon:		3.24

Miles Per Gallon:		 18.5
Miles Per Gallon:		 17.57
Miles Per Gallon:		 56.93

Continue (y/n)?:


    
# display a welcome message
print("The Miles Per Gallon application")
print()

choice = "y"
while choice.lower() == "y":
    # get input from the user
    trip_distance = float(input("Enter trip distance:\t\t"))
    miles_gallon = float(input("Enter miles gallon:\t\t"))
    cost_gallon = float(input("Enter cost per gallon:\t\t"))
    
    if trip_distance <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif miles_gallon <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_gallon <= 0:
        print("cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = miles_gallon
        gas_cost = round((trip_distance / miles_gallon), 2)
        cost_mile = round((gas_cost * cost_gallon), 2)
        print()
        print("Miles Per Gallon:\t\t", mpg)
        print("Miles Per Gallon:\t\t", gas_cost)
        print("Miles Per Gallon:\t\t", cost_mile)
    print()
    choice = input("Continue (y/n)?: ")
    print()


print("Bye")



