import fitz  # PyMuPDF
import re

def extract_text_and_metadata(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # ---- metadata ----
    meta = doc.metadata or {}
    metadata = {
        "Title": meta.get("title", "Not available"),
        "Author": meta.get("author", "Not available"),
        "Subject": meta.get("subject", "Not available"),
        "Pages": doc.page_count,
    }

    # ---- sentences for semantic search ----
    sentences = re.split(r'(?<=[.!?])\s+', full_text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    return full_text, metadata, sentences
