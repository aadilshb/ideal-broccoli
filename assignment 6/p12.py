c_held=int(input("Enter total classes held:"))
c_at=int(input("Enter classes attended:"))

attendance=(c_at/c_held)*100
if attendance>=75:
    print("Percentage:",attendance,"\nAllowed")
else:
    print("Percentage:",attendance,"\nNot allowed")
