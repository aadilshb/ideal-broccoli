lst=input("Enter elements:").split()
integers=[int(x) for x in lst if x.isdigit()]
floats=[float(x) for x in lst if '.' in x]
strings=[x for x in lst if not x.isdigit() and '.' not in x]

print("Integers:",integers)
print("Floats:",floats)
print("Strings:",strings)
