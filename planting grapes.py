row=int(input("enter the length of row in feet :"))
end_post=int(input("enter the space used by an end post in feet :"))
space=int(input("the amount of space between the vines in feet :"))
grapes=row-(2*end_post)/space
print("the number of grape vine fruit in a row is ",grapes)
