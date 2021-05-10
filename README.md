# Exam Templates

Template PDFs for University of Warwick's online exams to be imported into your favourite note taking application. An example of the template can be seen in `template.pdf`.

# Usage

## Script

The script `generate.py` will generate the pdfs for the modules you are taking and send the result to output. Simply run this script from inside the directory and the work will be done for you! All you need to do is set the modules, desired page number, and university ID in `config.json`.

## Single

One should edit `settings.tex` to set the userid and page numbers if they wish to output a single file. Then `pdflatex` can be used on `template.tex`.
