even_numbers = [num for num in range(1, 101) if num % 2 == 0]
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]

div_by_4 = [num for num in even_numbers if num % 4 == 0]
div_by_6 = [num for num in even_numbers if num % 6 == 0]
div_by_8 = [num for num in even_numbers if num % 8 == 0]
div_by_10 = [num for num in even_numbers if num % 10 == 0]

div_by_3 = [num for num in odd_numbers if num % 3 == 0]
div_by_5 = [num for num in odd_numbers if num % 5 == 0]
div_by_7 = [num for num in odd_numbers if num % 7 == 0]
div_by_9 = [num for num in odd_numbers if num % 9 == 0]

print("Numbers divisible by 4:", div_by_4)
print("Numbers divisible by 6:", div_by_6)
print("Numbers divisible by 8:", div_by_8)
print("Numbers divisible by 10:", div_by_10)
print("Numbers divisible by 3:", div_by_3)
print("Numbers divisible by 5:", div_by_5)
print("Numbers divisible by 7:", div_by_7)
print("Numbers divisible by 9:", div_by_9)
