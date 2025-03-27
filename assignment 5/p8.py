words = input("Enter words:").split()
max_length = 0
for word in words:
    if len(word)>max_length:
        max_length=len(word)
print("Longest:",max_length)