n=input("Enter numbers: ").split()
nu=[int(num) for num in n]
count=0
for num in nu:
    if num>30:
        count+= 1
print("Count of numbers greater than 30:", count)
