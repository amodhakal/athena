package main

import (
	"bytes"

	"github.com/dslipak/pdf"
)

func ReadPdf(path string) string {
	r, err := pdf.Open(path)
	if err != nil {
		panic(err)
	}

	var buf bytes.Buffer
	b, err := r.GetPlainText()
	if err != nil {
		panic(err)
	}

	buf.ReadFrom(b)
	return buf.String()
}
