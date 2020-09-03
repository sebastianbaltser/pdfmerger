# pylint: disable=E1120 #No value for argument ...

"""
Script that merges PDF-files
"""

import os
import re
import click
import PyPDF2

def pdfmerge(directory, output_filename):
    """
        Merges every pdf-file in the supplied directory.
        Ignores pdf-file that has the same filename as output_filename.
        Saves merged pdf-file to the same directory with filename output_filename.
    """
    os.chdir(directory)

    pdf_files = os.listdir('.')
    # Only pertain pdf files
    pdf_files = [fn for fn in pdf_files if fn.endswith('.pdf')]
    # Remove the file that was previously created by the script
    pdf_files = [fn for fn in pdf_files if fn != output_filename]

    # Sort by modification date
    pdf_files.sort(key=os.path.getctime)

    pdf_writer = PyPDF2.PdfFileWriter()

    writer_page_num = 0
    for filename in pdf_files:
        with open(filename, 'rb') as pdf_obj:
            pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
            for page_num in range(pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)
                if page_num == 0:
                    title = str(pdf_reader.getDocumentInfo().title)
                    if (title and title != 'None'):
                        title = strip_title(title)
                        pdf_writer.addBookmark(title, writer_page_num)
                    else:
                        pdf_writer.addBookmark(filename[:-4], writer_page_num)
                writer_page_num += 1

            with open(output_filename, 'wb') as pdf_output:
                pdf_writer.write(pdf_output)
                pdf_writer.addBlankPage()
                writer_page_num += 1

def strip_title(string):
    """Removes everything in parenthesis or brackets."""
    return re.sub(r'[\(\[][^()]*[\)\]]', '', string).strip()

@click.command()
@click.option("--directory", help="Location of PDF-files")
@click.option("-output", help="Name of output PDF-file")
def main(directory, output):
    """pdfmerger Console Script."""

    if output[-4:] != '.pdf':
        output = output + '.pdf'

    pdfmerge(directory, output)

    return 0

if __name__ == "__main__":
    main()
