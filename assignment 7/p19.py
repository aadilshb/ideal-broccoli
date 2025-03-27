lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
n_lst=[]

for l in lst:
    if l not in n_lst:
        n_lst.append(l)

print(n_lst)