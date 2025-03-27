s=input("Enter a string:")
n=int(input("Enter index:"))
new_s=""
for i in range(len(s)):
    if i!=n:
        new_s += s[i]
print(new_s)