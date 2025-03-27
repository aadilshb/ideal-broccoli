d1={'a':100,'b':200,'c':300}  
d2={'a':300,'b':200,'d':400}  
result=d1.copy()  

for key in d2:  
    if key in result:  
        result[key]+=d2[key]  
    else:  
        result[key]=d2[key]  

print(result)
