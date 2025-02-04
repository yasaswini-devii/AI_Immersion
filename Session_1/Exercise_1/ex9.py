from collections import Counter
import re

def most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower()) 
    counter = Counter(words)
    return counter.most_common(1)[0] if counter else None

text = "apple banana apple orange banana apple"
print(most_common_word(text)) 
