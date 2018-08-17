#!/usr/bin/env python3



# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
more = "y"
while more.lower() == "y":    
    trip_distance = float(input("Enter trip distance:\t\t"))
    miles_gallon = float(input("Enter miles_gallon used:\t"))
    cost_gallon = float(input("Enter cost per gallon:\t\t"))

    #Error input
    if trip_distance <= 0 or miles_gallon <= 0 or cost_gallon <= 0:
        print("Must enter greater than zero.")
        continue   
    
    # calculate miles per gallon
    mpg = miles_gallon
    gas_cost = round(trip_distance / miles_gallon, 2)
    cost_per_mile = round(gas_cost * cost_gallon, 2)
                
    # format and display the result
    print()
    print("Miles Per Gallon:\t" + str(mpg))
    print("Total Gas Cost:\t\t" + str(gas_cost))
    print("Cost Per Mile:\t\t" + str(cost_per_mile))

    more = input("continue? (y/n): ")
    print()
print("Bye!")


