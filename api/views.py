from django.shortcuts import render
from .pdf_processor import extract_text_and_metadata
from .ai_processor import summarize_text, semantic_search, build_semantic_index

# ---- GLOBAL STORAGE (Milestone 1 safe) ----
GLOBAL_SENTENCES = []
GLOBAL_TEXT = ""
GLOBAL_METADATA = {}
GLOBAL_SUMMARY = ""

def home(request):
    return render(request, "index.html")


def upload_pdf(request):
    global GLOBAL_SENTENCES, GLOBAL_TEXT, GLOBAL_METADATA, GLOBAL_SUMMARY

    if request.method == "POST" and request.FILES.get("pdf"):
        pdf = request.FILES["pdf"]

        text, metadata, sentences = extract_text_and_metadata(pdf)
        build_semantic_index(sentences)

        summary = summarize_text(text)

        # store globally
        GLOBAL_TEXT = text
        GLOBAL_METADATA = metadata
        GLOBAL_SENTENCES = sentences
        GLOBAL_SUMMARY = summary

        return render(request, "index.html", {
            "summary": summary,
            "metadata": metadata
        })

    return render(request, "index.html")

def search_view(request):
    global GLOBAL_SUMMARY, GLOBAL_METADATA

    results = []

    if request.method == "POST":
        query = request.POST.get("query")

        if query:
            results = semantic_search(query)

    return render(request, "index.html", {
        "summary": GLOBAL_SUMMARY,
        "metadata": GLOBAL_METADATA,
        "results": results
    })
