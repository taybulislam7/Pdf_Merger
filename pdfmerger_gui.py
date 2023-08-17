import PyPDF2
import tkinter as tk
from tkinter import filedialog

def merge_pdfs():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if not file_paths:
        return  # If no files selected, return without merging

    merger = PyPDF2.PdfMerger()
    for file_path in file_paths:
        pdf_file = open(file_path, 'rb')  # Open the PDF file in binary read mode
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        merger.append(pdf_reader)
        pdf_file.close()  # Close the file after appending its content

    destination_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if destination_path:
        with open(destination_path, 'wb') as merged_file:
            merger.write(merged_file)  # Write the merged PDF content to the new file

# Create the main application window
root = tk.Tk()
root.title("PDF Merger")

# Create the "Merge PDFs" button
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=10)

# Start the main event loop
root.mainloop()
