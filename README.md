# PyCabinet
---
A simple tool for file path management and searching. The creation of a cabinet object from a file path allows the user to easily filter, index and slice the contents of any directory and retrieve the full file path.


The initial plan is to keep PyCabinet doing a simple job; allow users to find file paths of specific files and folders in a systematic and userfriendly way.

Users of pandas should be familiar with the framework for filtering/slicing.

### Examples
---
```python 
import pycabinet as pc

c = pc.cabinet(r'/Users/Nick/downloads')
files = c.files()
print(files['.zip'])

>>> ['ParquetViewer_v1.1.0.0.zip', 'SQLiteStudio-3.2.1.zip']


print(files['.zip'][1])

>>> 'SQLiteStudio-3.2.1.zip'


print(files['Par'])

>>> 'ParquetViewer_v1.1.0.0.zip'

files = c.files(full_path=true)
print(files['.zip'])

>>> ['/Users/Nick/downloads/ParquetViewer_v1.1.0.0.zip', '/Users/Nick/downloads/SQLiteStudio-3.2.1.zip']
```    