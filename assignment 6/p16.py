lst=[int(x) for x in input("Enter numbers:").split()]
num=int(input("Enter the number to delete:"))

if num in lst:
    lst.remove(num)
    print(f"{num} deleted from the list.")
else:
    print(f"{num} not found in the list.")

print("Updated list:")
for i in lst:
    print(i)
