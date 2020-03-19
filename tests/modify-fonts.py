'''
Test for modifying font face and size
'''
import docx
from docx.shared import Pt

samples = './samples/valid/'

# see: https://www.programcreek.com/python/example/89765/docx.Document
# see: https://stackoverflow.com/questions/27884703/set-paragraph-font-in-python-docx
#Open the document
doc = docx.Document(samples + 'resume.docx')
style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(10)

#for p in doc.paragraphs:
#    font = p.font
#    font.name = 'Calibri'
#    font.size = Pt(10.5)

doc.save('/c/docs/resume2.docx')

