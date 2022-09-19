test_a =int(input("enter your first test score"))
test_b=int(input("enter your second test score"))
test=test_a + test_b
exam =int(input("enter your exam score"))
total = (test+exam)
if test_a <= 25:
    if test_b <= 25:
        if exam <=50:
            if total >=80 and total <=100:
                print(" your total point is",total,"and your  grade is A")
            elif total >=60 and total <=80:
                print("your total point is ",total,"and your grade is B")
            elif total >=50 and total<=59:
                print("your total point is ",total, "and your grade is C")
            else :
                print("your total point is ",total,"and your grade is F")
        else:
            print("enter valid exam score")
    else:
        print("enter valid secind test score")
else:
    print("enter valid first test score")