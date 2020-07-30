import pycabinet as pc

cabinet = pc.cabinet(r'\\NAS\Hard Drive\dev\db\identifiers')

files = cabinet.files()

print(files['.db'])