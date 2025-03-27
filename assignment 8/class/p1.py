class RomanConverter:
    def __init__(self):
        self.romans = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                       90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    
    def int_to_roman(self,num):
        result=""
        for value in sorted(self.romans.keys(),reverse=True):
            while num>=value:
                result+=self.romans[value]
                num-=value
        return result

    def roman_to_int(self, roman):
        roman_map={v:k for k,v in self.romans.items()}
        i,num=0,0
        while i<len(roman):
            if i+1<len(roman) and roman[i:i+2] in roman_map:
                num+=roman_map[roman[i:i+2]]
                i+=2
            else:
                num+=roman_map[roman[i]]
                i+=1
        return num

c=RomanConverter()
print(c.int_to_roman(58))
print(c.roman_to_int('LVIII'))
