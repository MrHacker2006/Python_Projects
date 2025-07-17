# 📎 PDF Merger Tool in Python

### 🤝Project Type: Made with Help

This is a simple Python script that merges multiple PDF files into a single PDF document using the **PyPDF2** library. It's a handy little utility when you need to combine reports, assignments, documents, or scanned pages into one clean file — all from the command line.

---

## 🛠️ What It Does

- Asks the user how many PDF files they want to merge  
- Takes file names one by one as input  
- Merges all the provided PDF files in the specified order  
- Saves the merged file as **`Merged-PDF.pdf`** in the current directory  

---

You can install `PyPDF2` using pip if you haven't already:

pip install PyPDF2

---  

##  🚀 How to Use
1.Save the script as merge_pdfs.py.

2.Place all the PDF files you want to merge in the same folder as the script.

3.Open terminal / command prompt and run the script:  python merge_pdfs.py

4.Enter the number of PDFs you want to merge when prompted.

5.Enter each PDF file name exactly (including the .pdf extension).
 For example: file1.pdf, document2.pdf, etc.

6.After processing, you will see a new file named:
✅ Merged-PDF.pdf


## 💡Example

```
How many PDF's you want to merge
3

Enter the name of the pdf 1: file1.pdf
Enter the name of the pdf 2: file2.pdf
Enter the name of the pdf 3: file3.pdf
```

