weight = int(input("Weight "))
unit = input("(K)g or (L)bs? ")

if unit.upper() == 'L':
    converted = weight / 2.25
    print("Your Weight in Kg " + str(converted))
if unit.upper() == 'K':
    converted = weight * 2.25
    print("Your weight in Lbs " + str(converted))


