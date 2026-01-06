from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .pdf_processor import extract_text_from_pdf

def home(request):
    return render(request, "index.html")

@csrf_exempt
def upload_pdf(request):
    if request.method == "POST":
        pdf_file = request.FILES.get("pdf")

        text = extract_text_from_pdf(pdf_file)

        print("TEXT LENGTH:", len(text))

        return JsonResponse({
            "extracted_text": text[:1500]
        })
