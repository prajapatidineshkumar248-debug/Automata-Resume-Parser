import pdfplumber
import re

pdf_path = input("Enter PDF file path: ")

with pdfplumber.open(pdf_path) as pdf:
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

print("\n----- Resume Details -----")

emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
phones = re.findall(r'\b\d{10}\b', text)

if emails:
    print("Email:", emails[0])
else:
    print("Email not found")

if phones:
    print("Phone:", phones[0])
else:
    print("Phone not found")
