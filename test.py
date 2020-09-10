import pycabinet as pc

cabinet = pc.cabinet(r'/Users/Nick/Downloads')

files = cabinet.files()

x = files['.dmg']

print(files['0'])