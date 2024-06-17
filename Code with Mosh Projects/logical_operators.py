high_income = True
good_credit = True

if high_income and good_credit:  # No need to have high_income == True because that variable is a bool and is already true
    print("Eligible")  # If one of the var's is false then it will output "Not Eligible"
else:
    print("Not Eligible")  # This will output "elgible"

high_income = True
good_credit = False

if high_income or good_credit:  # In this one if either high income or good credit are true then it will output "elgible"
    print("Eligible")
else:
    print("Not Eligible")

high_income = True
good_credit = False
student = True

if not student:  # This will only print "Elgible" is the student var is False
    print("Eligible")
else:
    print("Not Eligible")

high_income = True
good_credit = False
student = False

if (
        high_income or good_credit) and not student:  # need the () around first 2 vars to separate them from the and not student
    print("Eligible")
else:
    print("Not Eligible")
