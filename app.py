import streamlit as st
import spacy

from spacy.lang.en.stop_words import STOP_WORDS

import middleware

st.sidebar.title("Text Preprocessing")
text = st.sidebar.text_area("Enter Text")


if st.sidebar.button("Show Entire Analysis"):

    col1, col2 = st.columns(2)
    with col1:
        st.title("Stop Words")
        no_stopwords = middleware.stop_words(text)
        st.markdown(no_stopwords)

    with col2:
        st.title("No Punctuation")
        no_punct = middleware.punct(text)
        st.markdown(no_punct)

    col1,col2 = st.columns(2)
    with col1:
        st.title("Name & Entity")
        ner = middleware.ner_recog(text)
        st.markdown(ner)

    with col2:
        st.title("Lemmatization")
        lemma = middleware.lemmatization(text)
        st.markdown(lemma)


    st.title("Stemming of Sentence")
    stem = middleware.stemming(text)
    st.dataframe(stem)

    st.title("Parts of Speech tagging")
    pos = middleware.pos_tagging(text)
    st.dataframe(pos)


st.text("Specific Pre-processing of Text")
if st.button("Remove Stop Words"):
    no_stopwords = middleware.stop_words(text)
    st.markdown(no_stopwords)

if st.button("Remove Punctuation"):
    no_punct = middleware.punct(text)
    st.markdown(no_punct)

if st.button("Name Entity Recognition"):
    ner = middleware.ner_recog(text)
    st.markdown(ner)

if st.button("Lemma of Text"):
    lemma = middleware.lemmatization(text)
    st.markdown(lemma)

if st.button("Stemming of Words in text"):
    stem = middleware.stemming(text)
    st.dataframe(stem)

    # st.text(stem)

if st.button("Parts of Speech of words"):
    pos = middleware.pos_tagging(text)
    st.dataframe(pos)
