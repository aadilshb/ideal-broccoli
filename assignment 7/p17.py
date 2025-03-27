dict1 = {'key1': 1, 'key2': 3}
dict2 = {'key1': 1, 'key2': 2}

for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        print(f"{key} is present in both dictionaries")