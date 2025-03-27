words=input("Enter string:").split()
smallest=words[0]
largest=words[0]
for word in words:
    if len(word)<len(smallest):
        smallest=word
    if len(word)>len(largest):
        largest=word       
print("Smallest word:",smallest)
print("Largest word:",largest)