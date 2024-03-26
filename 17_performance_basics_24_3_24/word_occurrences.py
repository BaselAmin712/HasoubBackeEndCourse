from collections import Counter
import re

def count_word_occurrences(text):
    words = re.findall(r'\b\w+\b', text.lower())

    # Count occurrences of each word
    word_counts = Counter(words)

    return word_counts

# Example usage:
text = "This is a sample text. This text contains some sample words. Count occurrences of each word in this text."
word_occurrences = count_word_occurrences(text)
print(word_occurrences)