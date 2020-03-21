'''
Test for modifying font face and size
'''
import os
import docx
import pytest
from docx.shared import Pt

samples = './samples/valid/'
tmpdir = './samples/tmp/'
# see: https://www.programcreek.com/python/example/89765/docx.Document
# see: https://stackoverflow.com/questions/27884703/set-paragraph-font-in-python-docx
#Open the document
doc = docx.Document(samples + 'resume.docx')
style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(10)
fontfile = tmpdir + 'fonts.docx'
doc.save(fontfile)
doc = docx.Document(fontfile)
style = doc.styles['Normal']
font = style.font

def test_font_name():
    assert font.name == 'Arial'

def test_font_size():
    assert font.size == 127000

try:
    os.remove(fontfile)
except OSError as e:  ## if failed, report it back to the user ##
    print("Error: %s - %s." % (e.filename, e.strerror))
