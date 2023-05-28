# pdf-decrypter

This script allows you to decrypt multiple PDF files using QPDF. It automates the process of decrypting PDF files with the same password and saves the decrypted files to a specified output directory.

## Prerequisites

- QPDF: Make sure QPDF is installed on your system. You can download it from the official website: https://qpdf.sourceforge.io/

## Usage

1. Place the encrypted PDF files in a directory.
2. Run the script using the command `python PDFDecrypter.py`.
3. Enter the password, input directory, and output directory
4. The script will decrypt all the PDF files in the input directory using the specified password and save the decrypted files to the output directory.

## Script Details

- `password`: password used to decrypt the PDF files.
- `input_dir`: Path to the directory containing the encrypted PDF files.
- `output_dir`: Path to the directory where the decrypted PDF files will be saved.

## Limitation

- The encrypted files need to be in the same directory
- For encrypted files need to have the same password 


