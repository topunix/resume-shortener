import docx2txt
import pytest
import subprocess

sample_dir = './samples/invalid/'

def test_char_count():
    # extract text
    text = docx2txt.process(sample_dir + "shortresume.docx")
    value = len(text)
    assert value >= 1000


def test_page_length():
    onepage = sample_dir + 'onepage.docx'
    shell_command = f"unzip -p '{onepage}' docProps/app.xml | grep -oP '(?<=\<Pages\>).*(?=\</Pages\>)'"




