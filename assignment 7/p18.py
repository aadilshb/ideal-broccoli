list1=[{},{},{}]  
list2=[{1:2},{},{3:3}]  

empty1=True
empty2=True

for d in list1:
    if d:
        empty1=False
        break

for d in list2:
    if d:
        empty2=False
        break

print(empty1)
print(empty2)
