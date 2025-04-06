import PyPDF2

def pdf_to_text(pdf_file_path, text_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Initialize a string to hold the text
        text = ""
        
        # Loop through each page in the PDF
        for page in range(len(pdf_reader.pages)):
            # Extract text from the page
            text += pdf_reader.pages[page].extract_text() + "\n"
        
    # Write the extracted text to a text file
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

# Example usage
pdf_file_path = 'example.pdf'  # Path to your PDF file
text_file_path = 'output.txt'   # Path where you want to save the text file
pdf_to_text(pdf_file_path, text_file_path)

print(f"Text extracted and saved to {text_file_path}")