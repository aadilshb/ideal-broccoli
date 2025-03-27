total=0
product=1
count=0

while True:
    inp=input("Enter a number (or press 'q' to quit): ")   
    if inp.lower() == 'q':
        break
    num=int(inp)
    total+=num
    product*=num
    count+=1
if count>0:
    average=total/count
    print("Average:",average)
    print("Product:",product)
else:
    print("No numbers!")
