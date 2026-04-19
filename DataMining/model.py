from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import extract_text

def rank_resumes(resume_paths, job_desc):
    documents = [job_desc]

    resumes_text = []
    for path in resume_paths:
        text = extract_text(path)
        resumes_text.append(text)
        documents.append(text)

    tfidf = TfidfVectorizer(stop_words='english')
    matrix = tfidf.fit_transform(documents)

    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()

    results = []
    for i, score in enumerate(scores):
        results.append({
            "name": resume_paths[i].split("/")[-1],
            "score": round(score * 100, 2)
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results