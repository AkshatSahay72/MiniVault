from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_notes(notes):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(notes)
    return tfidf_matrix, vectorizer