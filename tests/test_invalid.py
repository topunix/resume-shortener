import docx2txt
import pytest
import subprocess

sample_dir = './samples/invalid/'

def test_min_char_count():
    # extract text
    text = docx2txt.process(sample_dir + "shortresume.docx")
    value = len(text)
    assert value >= 1000


'''
Couldn't get the unzip command working: file not found error. It works at command line
def test_page_length():
    onepage = sample_dir + 'onepage.docx'
    #shell_command = f"unzip -p '{onepage}' docProps/app.xml | grep -oP '(?<=\<Pages\>).*(?=\</Pages\>)'"
    shell_command = f"unzip"
    proc = subprocess.Popen(
        shell_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    output, error = proc.communicate()
    if error:
        errors = error.decode().split('\n')
        sys.exit(errors[0])
    value = output.decode()
    assert value > 1
'''
