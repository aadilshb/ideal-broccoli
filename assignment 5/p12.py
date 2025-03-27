s=input("Enter a string:")
count=0
for i in range(min(4, len(s))):
    if 'A'<=s[i]<='Z':
        count+=1
if count>=2:
    s=s.upper()
print(s)