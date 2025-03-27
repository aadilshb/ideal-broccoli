words=input("Enter words:").split(", ")
unique=[]
for word in words:
    if word not in unique:
        unique.append(word)
unique.sort()
print(", ".join(unique))