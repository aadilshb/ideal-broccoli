def find_substring(words,substring):
    return list(filter(lambda word:substring in word,words))

words=['red','black','white','green','orange']

substring=input("Enter string to search:")

matching_words=find_substring(words,substring)

print("Elements with substring:",matching_words)
