import string

with open("bath-livingston.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()

for symbol in string.punctuation + "—…“”":
    text = text.replace(symbol, " ")

words_list = text.split()

clean_list = []
for word in words_list:
    if word != "a" and word != "the":
        clean_list.append(word)

unique_dictionary = set(clean_list)

print("Total words:", len(clean_list))
print("Unique words:", len(unique_dictionary))
