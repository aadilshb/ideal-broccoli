s=input("Enter a string: ")
new_s=s[0]
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        new_s+=s[i]
print(new_s)