import os, fnmatch, copy

# Cabinet object class
class cabinet:
    """# Cabinet object
        Returns cabinet object from directory path. Allows for stacked searching and slicing of directory items. 
        
        Attributes:
        ----------
            path : str
                Directory path
            item : str {'cabinet', 'file', 'folder'}
                Type of cobinet object return. File and folder return pre-filtered object.
            full_path : bool
                
        
        Parameters:
        ----------
            path(str)
                Directory path.
            item(str) {'cabinet', 'file', 'folder'}
                Type of cabinet object to return.
            full_path(bool)
                Select whether full paths are returned.
            
        ## Returns
        ----------
            cls
                Returns cabinet class object
        
        
        ### Example:
            >>> cabinet = pc.cabinet(r'/Users/Nick/downloads')
            >>> print(cabinet['.dmg'])
            
        
        
    """  

    def __init__(self, path: str, item='cabinet', full_path=False):
        self.path = path
        self.instance = item
        self.full_path = full_path
        self.index = None
        self.inherited = None
        
    def __str__(self): return str(self._list)

    def __iter__(self): return iter(self._list)

    def __getitem__(self, index):
        new = copy.deepcopy(self)
        new.index = index
        new.inherited = new._indexed(new._list, new.index)
        return new
    
    @property
    def _list(self):
        # Use inherited cabinet list or create new one
        if self.inherited is None:
            # Init file list
            file_list = os.listdir(self.path)
            
            if self.instance=='file':
                file_list = self._listis(file_list, os.path.isfile)
            elif self.instance=='folder':
                file_list = self._listis(file_list, os.path.isdir)
            else: pass # complete directory list
            
        else: file_list = self.inherited

        # Append full path
        if self.full_path is True:
            file_list = self._join_path(file_list)
        else: pass

        return file_list

    def _listis(self, lst, func):
        check_path = lambda path: path if func(path) == True
        return map(check_path, lst)

    def _join_path(self, lst):
        add_path = lambda filename: os.path.join(self.path, filename)
        return list(map(add_path, lst))

    def _filter(self, lst, search_string):
        return fnmatch.filter(lst, "*" + search_string + "*")

    def _indexed(self, lst, idx):
        if isinstance(idx, (int, slice)): 
            try: return lst[idx]
            except IndexError: return None
        elif isinstance(idx, str):
            try: return self._filter(lst, idx)
            except IndexError: return None


    @property
    def latest(self):
        lst = self._append_path(self._list)
        return os.path.basename(max(lst, key=os.path.getctime, default="None"))

    def files(self, full_path=False):
        return cabinet(self.path, 'file', full_path)

    def folders(self, full_path=False):
        return cabinet(self.path, 'folder', full_path)

    def apply(self, func):
        pass