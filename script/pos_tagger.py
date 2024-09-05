import nltk

def train_pos_tagger(tagged_sents):
    trainer = nltk.UnigramTagger(tagged_sents)
    return trainer

if __name__ == "__main__":
    tagged_sentences = [
        [("word1", "NN"), ("word2", "VB"), ("word3", "JJ")],
        [("word4", "DT"), ("word5", "NN"), ("word6", "VB")]
    ]
    pos_tagger = train_pos_tagger(tagged_sentences)
    sentence = ["word1", "word4", "word6"]
    tagged_sentence = pos_tagger.tag(sentence)
    print("Tagged sentence:", tagged_sentence)
