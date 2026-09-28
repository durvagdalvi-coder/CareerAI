from pypdf import PdfReader
from docx import Document


def extract_text(file):

    filename = file.name.lower()

    text = ""


    if filename.endswith(".pdf"):

        reader = PdfReader(file)

        for page in reader.pages:
            text += page.extract_text() or ""



    elif filename.endswith(".docx"):

        document = Document(file)

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"



    elif filename.endswith(".txt"):

        text = file.read().decode(
            "utf-8"
        )



    return text