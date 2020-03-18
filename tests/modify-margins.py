'''
Test for modifying margins
'''
import docx
from docx.shared import Inches

samples = './samples/valid/'

#Open the document
document = docx.Document(samples + 'resume.docx')

#changing the page margins
sections = document.sections
for section in sections:
    section.top_margin = Inches(.25)
    section.bottom_margin = Inches(.25)
    section.left_margin = Inches(.25)
    section.right_margin = Inches(.25)

document.save('/c/docs/resume2.docx')

