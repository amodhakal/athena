from pypdf import PdfReader


def read_pdf_contents(input_file: str) -> str:
    reader = PdfReader(input_file)
    content = ""

    for page in reader.pages:
        content += page.extract_text()

    return content
