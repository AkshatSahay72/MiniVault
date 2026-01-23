from sklearn.metrics.pairwise import cosine_similarity
from vectorizer import vectorize_notes

def search_notes(query, notes, top_k = 3):
    tfidf_matrix, vectorizer = vectorize_notes(notes)
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, tfidf_matrix)[0]

    ranked = sorted(enumerate(similarity),
                    key=lambda x: x[1],
                    reverse=True)
    
    return ranked[:top_k]