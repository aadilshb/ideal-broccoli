def balanced(s):
    stack=[]
    pairs={')':'(',']':'[','}':'{'}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop()!=pairs[char]:
                return False
    return not stack

brack=input("Enter brackets:")
print(balanced(brack))
