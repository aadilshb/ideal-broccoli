numbers =[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
div_n=list(filter(lambda x:x%19==0 or x%13==0,numbers))

print("Divisible numbers are:" ,div_n)