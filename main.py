import PyPDF2

# Open the PDF file
with open('Sandesh_Narayan_Resume.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    
    # Extract text from each page
    for page in reader.pages:
        text += page.extract_text()

# Save the extracted text into a Markdown file
with open('README.md', 'w') as readme_file:
    readme_file.write("# Resume\n\n")
    readme_file.write(text)

print("README.md file generated from PDF.")
