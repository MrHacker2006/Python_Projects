from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many PDF's you want to merge\n"))

for i in range(0,n):
    name = input(f"Enter the name of the pdf {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged-PDF.pdf")
merger.close()
