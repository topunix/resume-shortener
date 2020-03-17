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
    shell_command = "unzip -p 'sample.docx' docProps/app.xml | grep -oP '(?<=\<Pages\>).*(?=\</Pages\>)'"




