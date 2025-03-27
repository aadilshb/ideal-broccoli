x=int(input("Enter side1:"))
y=int(input("Enter side2:"))
z=int(input("Enter side3:"))

if x==y==z:
    print("Equilateral Triangle")
elif x==y or y==z or x==z:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
