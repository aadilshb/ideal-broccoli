data = {1: 10, 2: 30, 3: 20}

asc = dict(sorted(data.items(), key=lambda x: x[1]))

desc = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

print("Ascending:", asc)
print("Descending:", desc)
