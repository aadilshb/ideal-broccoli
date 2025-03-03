from collections import Counter
def are_anagrams1(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)
def are_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
print(are_anagrams1("listen","silent"))
print(are_anagrams1("hello","heard"))
print(are_anagrams2("listen","silent"))
print(are_anagrams2("heard","hello"))