#A program that finds out when a restaurant will run out of burgers

burger_patties = 190
eat = 15
make = 7
hours = 0

while burger_patties > 0:

    print("Burger patties left:")
    print(burger_patties)
    burger_patties = burger_patties - eat
    burger_patties = burger_patties + make

    hours = hours + 1


print("The restaurant will run out of burger patties in " + str(hours) + " hours")

#===========================================================================
# Bonus: Deluxe burgers
#===========================================================================

burger_patties1 = 95 # half of the total
burger_patties2 = 95 # other half of the total
eat = 15
make = 7
hours = 0

while burger_patties1 > 0:

    print("Burger patties left for normal burgers:")
    print(burger_patties1)
    burger_patties1 = burger_patties1 - eat
    burger_patties1 = burger_patties1 + make

    hours = hours + 1

while burger_patties2 > 0:

    print("Burger patties left for deluxe burgers:")
    print(burger_patties2)
    burger_patties2 = burger_patties2 - eat * 2
    burger_patties2 = burger_patties2 + make

    hours = hours + 1


print("The restaurant will run out of burger patties in " + str(hours) + " hours")


if hours < 12:
    print("The restaurant cannot make it throuh a 12-hour day")