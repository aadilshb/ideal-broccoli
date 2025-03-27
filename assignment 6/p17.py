even=[]
odd=[]
prime=[]

for num in range(1,101):
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
    
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            prime.append(num)

print("Even Numbers:",even)
print("Odd Numbers:",odd)
print("Prime Numbers:",prime)
