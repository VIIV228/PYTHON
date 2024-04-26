import os
filename = "example.docx"
basename, extension = os.path.splitext(filename)
print(extension)