def calc_average(score):
    for x in range(5):
        total=0
        print("enter test score",x+1,end="")
        score=float(input(":"))
        total=total+score
        average=score/5
        return average
def determine_grade(score):
    if score >=90 and score<=100:
      grade =  print(" a")
    elif score >= 80 and score <=89:
       grade= print(" b")
    elif score >= 70 and score <=79:
      grade=print(" c")
    elif score >= 60 and score <=69:
      grade=print("d")
    else :
      grade=print(" e")
    return grade
