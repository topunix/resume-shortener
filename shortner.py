from docx import Document

document = Document('existing-document-file.docx')
document.save('new-file-name.docx')
