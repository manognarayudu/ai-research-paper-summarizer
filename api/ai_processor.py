from transformers import pipeline
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# =============================
# Milestone 2: Summarization
# =============================

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text):
    if len(text) > 3000:
        text = text[:3000]

    summary = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]


# =============================
# Milestone 3: Semantic Search
# =============================

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

FAISS_INDEX = None
FAISS_SENTENCES = []


def build_semantic_index(sentences):
    global FAISS_INDEX, FAISS_SENTENCES

    # remove empty/short sentences
    FAISS_SENTENCES = [s for s in sentences if len(s.strip()) > 20]

    if not FAISS_SENTENCES:
        FAISS_INDEX = None
        return

    embeddings = embedding_model.encode(FAISS_SENTENCES)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    FAISS_INDEX = faiss.IndexFlatL2(dimension)
    FAISS_INDEX.add(embeddings)


def semantic_search(query, top_k=5):
    if FAISS_INDEX is None:
        return []

    query_embedding = embedding_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = FAISS_INDEX.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(FAISS_SENTENCES):
            results.append(FAISS_SENTENCES[idx])

    return results
