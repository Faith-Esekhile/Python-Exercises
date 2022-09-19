length_a=int(input("enter length of first  rectangle:"))
length_b=int(input("enter length of second rectangle :"))
width_a=int(input("enter width of first rectangle"))
width_b=int(input("enter width of second rectangle"))
area_a=length_a*width_a
area_b=width_b*length_b
if area_a > area_b:
    print("first rectangle has greater area")
else:
    print("second rectangle has greater area")



