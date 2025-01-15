from PyPDF2 import PdfReader, PdfWriter

def split_pdf_by_ranges(input_pdf, output_files_and_ranges):
    """
    Splits a PDF into multiple files based on specified page ranges.

    Args:
        input_pdf (str): Path to the input PDF file.
        output_files_and_ranges (list of tuples): List of (output_file, page_range) tuples.
            - output_file (str): The name of the output file.
            - page_range (tuple): A tuple specifying the start and end page (inclusive).
    """
    # Load the input PDF
    reader = PdfReader(input_pdf)
    
    for output_file, page_range in output_files_and_ranges:
        writer = PdfWriter()
        
        # Extract the specified page range
        start, end = page_range
        for i in range(start - 1, end):  # PyPDF2 uses zero-based indexing
            writer.add_page(reader.pages[i])
        
        # Write the extracted pages to the output file
        with open(output_file, "wb") as f:
            writer.write(f)
        print(f"Created: {output_file}")

# Example usage
input_pdf = "book.pdf"
output_files_and_ranges = [
    ("part1.pdf", (30, 55)),
    ("part2.pdf", (56, 87)),
    ("part3.pdf", (88, 120)),
    ("part4.pdf", (121, 139)),
]

split_pdf_by_ranges(input_pdf, output_files_and_ranges)
