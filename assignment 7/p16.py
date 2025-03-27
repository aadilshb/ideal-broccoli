data={'a':100,'b':200,'c':300,'d':50}
values=list(data.values())  
top_3=[]  

while len(top_3)<3:  
    max_value=max(values)  
    top_3.append(max_value)  
    values.remove(max_value)  

print(top_3)
