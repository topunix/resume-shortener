shortener.py
--------------
This is a Python script which shortens resumes in Word XML format (docx). It shortens resumes by:

- Removing whitespace before and after the resume
- Shrinking the margins and font
- Deleting overused phrases ("References available upon request.")

It is intended to be run on the command line, on Linux/Unix and Windows.

Usage
-------------

To run:
```
python shortener.py resume.docx
```

This will produce a docx file (resume-short.docx) in the current working directory. The original file is untouched.
