is_valid=lambda s:(
    any(c.isupper() for c in s) and
    any(c.islower() for c in s) and
    any(c.isdigit() for c in s) and
    len(s)>=10                   
)

user_input=input("Enter a string: ")

if is_valid(user_input):
    print("Valid string")
else:
    print("Invalid string")