'''
Test for removing blank pages
'''
import docx
samples = "./samples/valid/"
#doc = docx.Document(samples + 'resume.docx')
doc = docx.Document("/c/docs/resume3.docx")
p = doc.paragraphs[5]
print(len(p.text)) # will be zero for blank lines
