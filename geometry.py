import circle 
import rectangle 
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5
def main():
    choice=0
    while choice != QUIT_CHOICE:
        display_menu()
        choice=int(input('enter your choice:'))
        if choice==AREA_CIRCLE_CHOICE:
            radius=float(input("enter the circles radius:"))
            print('The area is', circle.area(radius))
        elif choice== AREA_RECTANGLE_CHOICE:
            width=float(input("enter the rectangle's width"))
            length=float(input("enter the rectangle's length"))
            print("the area is",rectangle.area(width,length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width=float(input("enter the rectangle's width"))
            length=float(input("enter the rectangle's length"))
            print("the perimeter is",rectangle.perimeter(width.length))
        elif choice == QUIT_CHOICE:
            print("exiting program")
        else:
            print("error invalid selection")
def display_menu():
    print('menu')
    print("1) area of circle")
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
main()

        






















 
