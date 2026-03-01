import re
from collections import Counter


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zа-яё\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def tokenize(text):
    return text.split()


def unigram_analysis(words):
    counter = Counter(words)
    top3 = counter.most_common(3)
    return counter, top3


def bigram_analysis(words):
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    counter = Counter(bigrams)
    top5 = counter.most_common(5)
    return counter, top5


def char_analysis(text):
    counter = Counter(text.replace(" ", ""))
    ranked = counter.most_common()
    return ranked


def analyze_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    cleaned = clean_text(text)
    words = tokenize(cleaned)

    unigram_dict, top3_words = unigram_analysis(words)
    bigram_dict, top5_bigrams = bigram_analysis(words)
    char_rank = char_analysis(cleaned)

    return top3_words, top5_bigrams, char_rank


eng_top3, eng_top5_bi, eng_chars = analyze_file("bester-eng.txt")
rus_top3, rus_top5_bi, rus_chars = analyze_file("bester-rus.txt")

print("English Top-3 words:", eng_top3)
print("English Top-5 bigrams:", eng_top5_bi)
print("English Character ranking:", eng_chars)

print("Russian Top-3 words:", rus_top3)
print("Russian Top-5 bigrams:", rus_top5_bi)
print("Russian Character ranking:", rus_chars)
