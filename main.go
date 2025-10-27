package main

const TEST_PDF_LOCATION = "./tests/1.pdf"

func main() {
	content := ReadPdf(TEST_PDF_LOCATION)
	println(content)
}
