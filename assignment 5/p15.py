s=input("Enter a string: ")
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
for i in freq:
    if freq[i]>1:
        print(i+" "+str(freq[i]))