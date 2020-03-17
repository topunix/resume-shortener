import docx2txt
import pytest

sample_dir = './samples/valid/'

def test_counts():
    text = docx2txt.process(sample_dir + "shortresume.docx")
    value = len(text)
    assert value >= 1000

