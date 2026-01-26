from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def summarize_text(text):
    # simple extractive summary
    sentences = text.split(". ")
    return ". ".join(sentences[:6]) + "."

def semantic_search(query, sentences, top_k=5):
    query_emb = model.encode(query, convert_to_tensor=True)
    sent_embs = model.encode(sentences, convert_to_tensor=True)

    scores = util.cos_sim(query_emb, sent_embs)[0]
    top_results = scores.topk(k=min(top_k, len(sentences)))

    results = []
    for idx in top_results.indices:
        results.append(sentences[int(idx)])

    return results
