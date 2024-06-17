high_income = False
good_credit = True
student = True


    if high_income and good_credit and not student:  #The compiler reads this statement from left to right, if one of them is not true it stops there and ignores the rest to the right of it.
    if high_income or good_credit or not student: # The compiler will keep reading if the first statement it false because of the or operator.