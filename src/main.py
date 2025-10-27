from google.genai.errors import ClientError
from src.io import read_pdf_contents
from src.ai import filter_contents


INPUT_FILE = "tests/1.pdf"


def main():
    content = read_pdf_contents(INPUT_FILE)
    try:
        filtered_content = filter_contents(content)
    except ClientError as client_err:
        print("Couldn't filter contents: ", client_err)
        return

    print(filtered_content)


if __name__ == "__main__":
    main()
