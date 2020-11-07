# PyCabinet: directories as an object

A simple tool for file path management and discovery. The creation of a cabinet object from a file path allows the user to easily filter, index and slice the contents of any directory.

Users of pandas should be familiar with the framework for filtering/slicing demonstrated in the examples below.


## How to Install

PyCabinet can be easily installed using pip:
```bash
pip install pycabinet
```

## Examples

```python 
>>> import pycabinet as pc

>>> c = pc.cabinet(r'/Users/Nick/downloads')
>>> files = c.files()
>>> print(files['.zip'])
['ParquetViewer_v1.1.0.0.zip', 'SQLiteStudio-3.2.1.zip']

>>> print(files['.zip'][1])
'SQLiteStudio-3.2.1.zip'

>>> print(files['Par'])
'ParquetViewer_v1.1.0.0.zip'

>>> files = c.files(full_path=true)
>>> print(files['.zip'])
['/Users/Nick/downloads/ParquetViewer_v1.1.0.0.zip', '/Users/Nick/downloads/SQLiteStudio-3.2.1.zip']
```    

## Future Development

The initial plan is to keep PyCabinet doing a simple job; allow users to find file paths of specific files and folders in a systematic and userfriendly way.

If it proves popular and there is demand for it, functionality could be expanded to include the ability to manipulate folders and files.