from pypdf import PdfReader


def extract_text(file):

    text = ""

    if file.name.endswith(".pdf"):

        pdf_reader = PdfReader(file)

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

    elif file.name.endswith(".txt"):

        text = file.read().decode("utf-8")

    return text