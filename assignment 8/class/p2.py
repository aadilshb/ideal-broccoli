class Parentheses:
    def is_valid(self,s):
        stack=[]
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                last=stack.pop()
                if(char==')'and last!='(') or (char=='}' and last!='{') or (char==']' and last!='['):
                    return False
        return not stack  

p = Parentheses()
print(p.is_valid("()[]{}"))
print(p.is_valid("(]"))
