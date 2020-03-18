'''
Test for modifying margins
'''
import docx
from docx.shared import Inches

samples = './samples/valid/'

#Open the document
document = Document(args.inputFile)

#changing the page margins
sections = document.sections
for section in sections:
    section.top_margin = Cm(margin)
    section.bottom_margin = Cm(margin)
    section.left_margin = Cm(margin)
    section.right_margin = Cm(margin)

document.save(args.outputFile)

