data=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
s_data=sorted(data,key=lambda x:int(x['model']))

print(data,"\n\n\n")
print(s_data)