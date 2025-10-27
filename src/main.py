from pypdf import PdfReader

INPUT_FILE = "tests/1.pdf"
OUTPUT_FILE = "tests/output.txt"

reader = PdfReader(INPUT_FILE)
content = ""

for page in reader.pages:
    content += page.extract_text()

with open(OUTPUT_FILE, "w") as f:
    f.write(content + "\n")
