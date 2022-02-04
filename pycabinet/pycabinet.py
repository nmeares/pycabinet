import os, fnmatch, copy

# Cabinet object class
class cabinet:
    """# Cabinet object
        Returns cabinet object from directory path. Allows for stacked searching and slicing of directory items. 
        
        Attributes:
        ----------
            root : str
                Directory root path
            instance : str {'cabinet', 'file', 'folder'} , optional
                Type of cabinet object return. File and folder return pre-filtered object.
            full_path : bool
                True if file/folder names with root path to be returned, False if only name to be returned.
                
        Methods:
        ----------
            folders(full_path=False):
                Returns cabinet object pre-filtered for folders. Equivalent to setting instance = 'folder'
            
            files(full_path=False):
                Returns cabinet object pre-filtered for folders. Equivalent to setting instance = 'file'
                
            latest():
                Returns latest file or folder by modified date
    """  
    def __init__(self, path: str, instance='cabinet', full_path=False):
        """ Constructs all attributes for the cabinet object.
        Parameters:
        ----------
            path: str
                Directory path.
            item : str {'cabinet', 'file', 'folder'}
                Type of cabinet object to return.
            `full_path` : bool
                Select whether full paths are returned.
            
        Returns:
        ----------
            Object
                Returns cabinet class object
        
        Example:
        ----------
            >>> cabinet = pc.cabinet(r'/Users/Nick/downloads')
            >>> print(cabinet['.zip'])
            ['ParquetViewer_v1.1.0.0.zip', 'SQLiteStudio-3.2.1.zip']
        """
        self.root = path
        self.instance = instance
        self.full_path = full_path
        self._index = None
        self._inherited = None
        
    def __str__(self): return str(self._list)

    def __iter__(self): return iter(self._list)

    def __getitem__(self, index):
        # Create deepcopy of cabinet object to be returned
        new = copy.deepcopy(self)
        new._index = index # Store index in new object
        # Indexed list stored in inherited attribute to allow for recursive indexing
        new._inherited = new._indexed(new._list, new._index)
        return new
    
    @property
    def _list(self):
        # Use inherited cabinet list or create new one
        if self._inherited is None:
            # Init file list
            file_list = os.listdir(self.root)
            # Return list based on cabinet sub-type
            if self.instance=='file':
                file_list = self._listis(file_list, os.path.isfile)
            elif self.instance=='folder':
                file_list = self._listis(file_list, os.path.isdir)
            else: pass # return complete dir list
            
        else: file_list = self._inherited

        # Append full path
        if self.full_path is True:
            file_list = self._join_path(file_list)
        else: pass

        return file_list

    def _listis(self, lst, func):
        # Create function apply os.path 'is' function to file path - return bool
        check = lambda filename: func(self._join_path(filename))
        # Return filtered list (using boolean mask)
        return list(filter(check, lst))

    def _join_path(self, item):
        try:
            if isinstance(item, list):
                return list(map(self._join_path, item))
            elif isinstance(item, str):
                return os.path.join(self.root, item)
        except TypeError: return None
         
    def _filter(self, lst, search_string):
        # Built in string filter function
        return fnmatch.filter(lst, "*" + search_string + "*")

    def _indexed(self, lst, idx):
        # Index object based on type
        if isinstance(idx, (int, slice)): 
            try: return lst[idx]
            except IndexError: return None
        elif isinstance(idx, str):
            try: return self._filter(lst, idx)
            except IndexError: return None


    @property
    def latest(self):
        # Allows user to retrieve latest file based on created time
        lst = self._join_path(self._list)
        return os.path.basename(max(lst, key=os.path.getctime, default="None"))

    # Cabinet type functions (alternative to using the function param)
    def files(self, full_path=False):
        return cabinet(self.root, 'file', full_path)

    def folders(self, full_path=False):
        return cabinet(self.root, 'folder', full_path)