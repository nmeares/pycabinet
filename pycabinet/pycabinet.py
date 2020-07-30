import os, fnmatch, copy

#TODO: move inner cabinet class out/ file and folder functions inside. _cabinet becomes main class.

# Cabinet object class
class cabinet:
    def __init__(self, path: str, item='cabinet', full_path=False):
        self.path = path
        self.item = item
        self.full_path = full_path
        self.all = self._list()
        
    def __str__(self): return str(self.all)

    def __iter__(self): return iter(self.all)

    def __getitem__(self, index):
        if type(index) == int: 
            try: return self.all[index]
            except IndexError: return None
        else:
            new = copy.deepcopy(self)
            new.all = [f for f in self.all if fnmatch.fnmatch(f, "*" + index + "*")==True]
            return new

    def _list(self):
        # Init file list
        if self.item=='file':
            file_list = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,f))]
        elif self.item=='folder':
            file_list = [f for f in os.listdir(self.path) if os.path.isdir(os.path.join(self.path,f))]
        else:
            file_list = os.listdir(self.path)

        # Add full path
        if self.full_path is True:
            file_list = [os.path.join(self.path, filename) for filename in file_list]
        else: pass
        return file_list

    @property
    def latest(self):
        lst = [os.path.join(self.path, filename) for filename in self.all]
        return os.path.basename(max(lst, key=os.path.getctime, default="None"))

    def files(self, full_path=False):
        return cabinet(self.path, 'file', full_path)

    def folders(self, full_path=False):
        return cabinet(self.path, 'folder', full_path)