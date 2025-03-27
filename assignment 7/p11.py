data={3:'C',1:'A',2:'B',5:'G',7:'K'}
s_data ={}
keys=list(data.keys())

while keys:
    min_key=min(keys)
    s_data[min_key]=data[min_key]
    keys.remove(min_key)

print(s_data)
