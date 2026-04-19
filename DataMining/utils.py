import PyPDF2

def extract_text(path):
    text = ""
    if path.endswith(".pdf"):
        with open(path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    return text