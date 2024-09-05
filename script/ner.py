def custom_ner_tagger(sentence):
    named_entities = []
    for word in sentence:
        if word.istitle():  # Simple rule: if the word is capitalized, it might be a named entity
            named_entities.append((word, "ENTITY"))
        else:
            named_entities.append((word, "O"))  # 'O' for non-entity
    return named_entities

if __name__ == "__main__":
    sentence = ["John", "went", "to", "Paris"]
    ner_tags = custom_ner_tagger(sentence)
    print("NER tags:", ner_tags)
