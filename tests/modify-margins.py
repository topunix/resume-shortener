'''
Test for modifying margins
'''
import os
import docx
from docx.shared import Inches

samples = './samples/valid/'
tmpdir = './samples/tmp/'

#Open the document
doc = docx.Document(samples + 'resume.docx')

#changing the page margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(.25)
    section.bottom_margin = Inches(.25)
    section.left_margin = Inches(.25)
    section.right_margin = Inches(.25)

marginfile = tmpdir + 'margins.docx'
doc.save(marginfile)
doc = docx.Document(marginfile)
margin_value = 228600

def test_margins_size():
    sections = doc.sections
    for section in sections:
        assert section.top_margin == margin_value
        assert section.bottom_margin == margin_value
        assert section.left_margin == margin_value
        assert section.right_margin == margin_value


try:
    os.remove(marginfile)
except OSError as e:  ## if failed, report it back to the user ##
    print("Error: %s - %s." % (e.filename, e.strerror))
