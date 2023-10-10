text = input("Введите текст: ")
words = text.split()
filtered_text = ""
for word in words:
    if not word.endswith('а') and not word.endswith('А') and not word.endswith('a') and not word.endswith(
            'A') and word.isalpha():
        filtered_text += word + " "

print("Текст без слов, заканчивающихся на 'а' или 'А':", filtered_text)
