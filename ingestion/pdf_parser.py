import PyPDF2
import json
import os

def parse_pdf(pdf_path, output_path):
    extracted_text = ""

    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"

    data = {
        "file_name": os.path.basename(pdf_path),
        "extracted_text": extracted_text
    }

    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print("PDF parsed successfully")
    print("Output saved to:", output_path)

if __name__ == "__main__":
    pdf_path = "sample_paper.pdf"
    output_path = "outputs/parsed_text.json"
    parse_pdf(pdf_path, output_path)
