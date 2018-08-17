#!/usr/bin/env python3

The Miles Per Gallon program

Enter trip distance:		500
Enter miles_gallon used:	50
Enter cost per gallon:		3.24

Miles Per Gallon:	50.0
Total Gas Cost:		10.0
Cost Per Mile:		32.4

Bye!


# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
trip_distance = float(input("Enter trip distance:\t\t"))
miles_gallon = float(input("Enter miles_gallon used:\t"))
cost_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_gallon
gas_cost = round(trip_distance / miles_gallon, 2)
cost_per_mile = round(gas_cost * cost_gallon, 2)
            
# format and display the result
print()
print("Miles Per Gallon:\t" + str(mpg))
print("Total Gas Cost:\t\t" + str(gas_cost))
print("Cost Per Mile:\t\t" + str(cost_per_mile))
print()
print("Bye!")


