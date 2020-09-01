# pylint: disable=E1120 #No value for argument ...

"""
Script that merges PDF-files
"""

import os
import re
import sys

import click

import PyPDF2

def merge(directory, mergeFilename):
    pdf_files = [fn for fn in os.listdir('.') if (fn.endswith('.pdf') and not fn == mergeFilename)]

    pdf_files.sort(key=str.lower)

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

            with open(mergeFilename, 'wb') as pdf_output:
                pdf_writer.write(pdf_output)
                pdf_writer.addBlankPage()
                writer_page_num += 1

def strip_title(string):
    """Removes everything in parenthesis or brackets."""
    return re.sub(r'[\(\[][^()]*[\)\]]', '', string)

if __name__ == "__main__":
    directory = os.environ["dir"]
    os.chdir(directory)
	 
    mergeFilename = os.environ["filename"]
    if mergeFilename[-4:] != '.pdf':
        mergeFilename = mergeFilename + '.pdf'

    merge(directory, mergeFilename)


@click.command()
@click.option("")
def main(*args, **kwargs):
    """pdfmerger Console Script."""
    click.echo("Replace this message by putting your code into "
               "pdfmerger.py")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
