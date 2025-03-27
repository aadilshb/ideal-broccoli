s = input("Enter a string: ")

not_pos = -1
poor_pos = -1

for i in range(len(s) - 2):
    if s[i:i+3] == "not":
        not_pos = i
    if s[i:i+4] == "poor":
        poor_pos = i

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    s = s[:not_pos] + "good" + s[poor_pos+4:]

print(s)
