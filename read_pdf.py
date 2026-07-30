import fitz  # this is PyMuPDF's internal name

def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    doc.close()
    return full_text


# Test it
if __name__ == "__main__":
    text = extract_text_from_pdf("documents/PatientAdmission.pdf")
    print(text)


   


    