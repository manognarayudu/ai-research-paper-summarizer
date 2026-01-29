from django.shortcuts import render
from .pdf_processor import extract_text_and_metadata
<<<<<<< HEAD
from .ai_processor import summarize_text, semantic_search, build_semantic_index
=======
from .ai_processor import summarize_text, semantic_search
>>>>>>> 9bff32eb85289445a476d131e03ebd3f03d2dc12

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
<<<<<<< HEAD
        build_semantic_index(sentences)

=======
>>>>>>> 9bff32eb85289445a476d131e03ebd3f03d2dc12
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

<<<<<<< HEAD
def search_view(request):
    global GLOBAL_SUMMARY, GLOBAL_METADATA
=======

def search_view(request):
    global GLOBAL_SENTENCES, GLOBAL_TEXT, GLOBAL_METADATA, GLOBAL_SUMMARY
>>>>>>> 9bff32eb85289445a476d131e03ebd3f03d2dc12

    results = []

    if request.method == "POST":
        query = request.POST.get("query")

<<<<<<< HEAD
        if query:
            results = semantic_search(query)
=======
        if query and GLOBAL_SENTENCES:
            results = semantic_search(query, GLOBAL_SENTENCES)
>>>>>>> 9bff32eb85289445a476d131e03ebd3f03d2dc12

    return render(request, "index.html", {
        "summary": GLOBAL_SUMMARY,
        "metadata": GLOBAL_METADATA,
        "results": results
    })
