total=0
count=0
while True:
    num=int(input("Enter a number (press 0 to finish):"))
    if num==0:
        break
    total+=num
    count+=1
if count > 0:
    print("Sum:",total,"Average:",total/count)
