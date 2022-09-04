import pprint
from .item_class import item
from pathlib import Path

class File(item):
    ''' Class Summary
    
    __new__
    
    New validates that the path is a valid fILE path
    Before even creating the object
    
    p = File(bad/path/) will return an error


    '''
   
    def __new__(cls, _path):
        if File.isFileOrError(_path):
            inst = object.__new__(cls)
            return inst

    def __init__(self, _path) -> None:
        super().__init__(_path)
        self.size = self.getSize(_path)
        self.fullName = Path(_path).name
    
    def __repr__(self) -> str:
        me = {
            'Name': self.fullName,
            'Path' : self.location,
            'size' : self.size['megabytes'],
        }
        return pprint.pformat(me)
    
    
    '''Properties'''

    '''Funcs'''
    def mkMyDir(self):
        self.mkdir(self.name, self.location)
    

    '''WIP'''
    def mkdirMoveFile(self):
        pass

    def duplicate(self):
        pass

    def delSelf(self):
        pass
    
    def dateCreated(self):
        pass
    
    def dateLastModified(self):
        pass
