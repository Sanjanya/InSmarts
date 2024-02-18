import spacy

nlp = spacy.load('en_core_web_sm')

def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.lemma_.lower().strip() for token in doc if token.is_stop != True and token.is_punct != True]
    return ', '.join(keywords)