import pandas as pd
import spacy

from spacy.lang.en.stop_words import STOP_WORDS
import en_core_web_sm
nlp = en_core_web_sm.load()
# nlp = spacy.load("en_core_web_sm")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def stop_words(text):
    doc = nlp(text)

    no_stop_words = [token.text for token in doc if not token.is_stop]
    return " ".join(no_stop_words)

def punct(text):
    doc = nlp(text)

    no_punct = [token.text for token in doc if not token.is_punct]
    return " ".join(no_punct)

def ner_recog(text):
    doc = nlp(text)

    ner_text = pd.DataFrame([[ent.text,ent.label_]] for ent in doc.ents])
    return ner_text

def lemmatization(text):
    doc = nlp(text)

    lemma = [token.lemma_ for token in doc]
    return " ".join(lemma)


def stemming(text):
    # doc = nlp(text)
    # l = []
    # stem = pd.DataFrame([[word, stemmer.stem(word)] for word in str])

    def Convert(string):
        li = list(string.split(" "))
        return li

    # Driver code
    str1 = Convert(text)

    stemming = pd.DataFrame([[word, stemmer.stem(word)] for word in str1])

    # for word in str1:
    #     s = stemmer.stem(word)
    #     stemi = pd.DataFrame(word,s)

    return stemming



def pos_tagging(text):
    doc = nlp(text)

    pos = pd.DataFrame([[token, token.pos_, spacy.explain(token.pos_), token.tag_, spacy.explain(token.tag_)] for token in doc])
    return pos
