def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    if len(str1) != len(str2):
        return False

    char_count1 = {}
    char_count2 = {}

    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    return char_count1 == char_count2

str1 = input("Введите первое строку: ")
str2 = input("Введите второе строку: ")
if are_anagrams(str1, str2):
    print("Эти строки являются анаграммами.")
else:
    print("Эти строки не являются анаграммами.")
