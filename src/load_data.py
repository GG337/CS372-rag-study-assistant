from pypdf import PdfReader
import re

def clean_text(text):
    # normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    # remove weird unicode/math symbols (optional but helpful)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  # avoid None issues
            text += page_text + "\n"

    return clean_text(text)