import pycabinet as pc

cabinet = pc.cabinet(r'/mnt/c/users/nickm/Downloads')

files = cabinet.files()

x = files['.zip']

print(x[5:8])
