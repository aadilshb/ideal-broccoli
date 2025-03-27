data={1:10,2:20,3:30,4:40,5:50}
print(data)
keyi=int(input("Key to Remove:"))

if keyi in data:
    del data[keyi]

print(data)
