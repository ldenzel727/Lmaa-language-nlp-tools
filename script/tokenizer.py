import re

def custom_sentence_tokenizer(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences

def custom_word_tokenizer(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return words

if __name__ == "__main__":
    text = "Example text in a low-resource language. This should be replaced with your own text."
    sentences = custom_sentence_tokenizer(text)
    print("Sentences:", sentences)
    for sentence in sentences:
        words = custom_word_tokenizer(sentence)
        print("Words in sentence:", words)
