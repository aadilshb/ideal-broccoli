lst=[19,'red',12,'green','blue',10,'white','green',1]

s_lst=sorted(lst,key=lambda x:(isinstance(x, str),x))

print("Sorted mixed list:",s_lst)
