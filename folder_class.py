# 8.7.22
from dataclasses import dataclass
from typing import List
from .item_class import item
from pathlib import Path
import os
import subprocess
import pprint

@dataclass
class Folder(item):

    def __post_init__(self):
        item.isFolderOrError(self.path)
        self.size = self.getSize(self.path)
        return super().__post_init__()
    
    def __repr__(self) -> str:
        me = {
            'Name': self.name,
            'Path' : self.path,
            'size' : self.size['megabytes'],
            'children': self.ls()
        }
        return pprint.pformat(me)
    
    
    '''Properties'''
    @property
    def lastModifiedFile(self):
        return self.getLastModifiedFile()
    
    @property
    def biggestFile(self):
        pass
    
    @property
    def smallestFile(self):
        pass
    
    @property
    def earliestModifiedFile(self):
        pass
    
    
    '''Funcs'''
    def ls(self, format= True):
        if format:
            return pprint.pformat([item for item in Path(self.path).iterdir()])
        else: 
            return [item for item in Path(self.path).iterdir()]
    def lsfil(self, format= True):
        if format:
            return pprint.pformat([item for item in Path(self.path).iterdir() if item.is_file()])
        else: 
            return [item for item in Path(self.path).iterdir() if item.is_file()]
    def lsdir(self, format= True):
        if format:
            return pprint.pformat([item for item in Path(self.path).iterdir() if item.is_dir()])
        else: 
            return [item for item in Path(self.path).iterdir() if item.is_dir()]
        
    def getLastModifiedFile(self):
        latest_file = max(self.lsfil(format=False), key=os.path.getctime)
        return latest_file
    
    def open(self):
        subprocess.Popen(f'explorer {self.path}')
    
    
    '''----------------UTIL FUNCTIONS-------------------------'''
    def forEachFile(self,callBack):
        '''
        map(self.lsfil(), callBack)
        '''
        for path in self.lsfil():
            callBack(path)
    
    def allFoldersExistsOrError(self,arrayOfFolders: List):
        for folder in arrayOfFolders:
            Folder.isFolderOrError(folder)
        return True
    
    def allFoldersExists(self,arrayOfFolders: List) -> bool:
        answer = True
        for folder in arrayOfFolders:
            try:
                Folder.isFolderOrError(folder)
            except:
                answer = False
        return answer

    def fileInFolder(self,fileName):
        pass





