import os
import sys
import fitz  # PyMuPDF

def arbitrary_sort(files = [], search_keys = ["_Red_","_Ylw_","_Grn_","_Chk_"]):
    # Sort the files by search keys in the order of the search keys
    sorted_files = []
    for key in search_keys:
        for file in files:
            if key in file:
                sorted_files.append(file)
    return sorted_files            

def package_pdfs(folder_path):
    # Create a dictionary to hold the packages
    packages = {}

    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Arrange PDFs into packages based on the prefix before the first underscore
    for pdf_file in pdf_files:
        prefix = pdf_file.split('_')[0]
        if prefix not in packages:
            packages[prefix] = []
        packages[prefix].append(os.path.join(folder_path, pdf_file))

    # Sort every package's files using arbitrary_sort function
    for prefix in packages: packages[prefix] = arbitrary_sort(packages[prefix])

    # Create 'packages' directory inside the original folder path
    packages_dir = os.path.join(folder_path, 'packages')
    os.makedirs(packages_dir, exist_ok=True)

    # Staple PDFs into multi-page PDFs and write to 'packages' directory
    # for prefix, files in packages.items():
    #     output_pdf_path = os.path.join(packages_dir, f"{prefix}.pdf")
    #     output_pdf = fitz.open()

    #     for pdf_path in files:
    #         input_pdf = fitz.open(pdf_path)
    #         for page_num in range(len(input_pdf)):
    #             page = input_pdf.load_page(page_num)
    #             rect = fitz.Rect(0, 0, 612, 792)  # Set page size to 8.5" x 11"
    #             new_page = output_pdf.new_page(width=rect.width, height=rect.height)
    #             new_page.show_pdf_page(rect, input_pdf, page_num)  # Scale page content to fit the new size

    #     output_pdf.save(output_pdf_path)
    #     output_pdf.close()

    # Staple PDFs into multi-page PDFs and write to 'packages' directory
    for prefix, files in packages.items():
        output_pdf_path = os.path.join(packages_dir, f"{prefix}.pdf")
        output_pdf = fitz.open()

        for pdf_path in files:
            input_pdf = fitz.open(pdf_path)
            for page_num in range(len(input_pdf)):
                page = input_pdf.load_page(page_num)
                # Set page size to 8.5" x 11" with 1-inch margins
                rect = fitz.Rect(36, 36, 576, 756)  # 72 points = 1 inch
                new_page = output_pdf.new_page(width=612, height=792)
                new_page.show_pdf_page(rect, input_pdf, page_num)  # Scale page content to fit the new size with margins

        output_pdf.save(output_pdf_path)
        output_pdf.close()


# Example usage, folder passed as an argument
folder_path = sys.argv[1] if len(sys.argv) > 1 else "C:\\Users\\lgiroux\\OneDrive - Barton Malow\\Desktop\\gComply Example PDFs" # Example
package_pdfs(folder_path)
