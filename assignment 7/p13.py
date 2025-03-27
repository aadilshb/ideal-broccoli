data={'a':10,'b':20,'c':10,'d':30}
n_data={}

for key in data:
    if data[key] not in n_data.values():
        n_data[key] = data[key]

print(n_data)
