'''
Test for removing blank pages
'''
import re
import docx
samples = "./samples/valid/"
#doc = docx.Document(samples + 'resume.docx')
# https://github.com/python-openxml/python-docx/issues/33

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None


doc = docx.Document("references.docx")
pattern = re.compile("references available", re.IGNORECASE)
paragraphs = [p for p in doc.paragraphs if not pattern.search(p.text)]


for idx,p in enumerate(doc.paragraphs):
    if pattern.search(p.text):

p = doc.paragraphs[5]
print(len(p.text)) # will be zero for blank lines
