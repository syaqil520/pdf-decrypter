import os
import subprocess


def decrypt_pdfs(password, input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pdf"):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_decrypted.pdf")
            try:
                result = subprocess.run(["qpdf", "--password=" + password, "--decrypt", input_file, output_file])
                if result.returncode == 0:
                    print(f"{file_name} decrypted")
                else:
                    print(f"Failed to decrypt {file_name}")
            except subprocess.CalledProcessError as e:
                print(f"QPDF failure: {e}")

def print_box(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    horizontal_line = '+' + '-' * (max_length + 2) + '+'

    print(horizontal_line)
    for line in lines:
        padding = max_length - len(line)
        print(f'| {line}{" " * padding} |')
    print(horizontal_line)

def main():
    print("PDF Decrypter script for QPDF\n")
    print_box("This can only be used alongside QPDF and the files with the same password")
    print("\nMake sure the encrypted files is in the same folder and the files have the same password\n")
    password = input("Enter file password: ")
    input_dir = input("Enter the folder directory: ")
    output_dir = input("Enter the output folder directory: ")

    decrypt_pdfs(password, input_dir, output_dir)


if __name__ == "__main__":
    main()