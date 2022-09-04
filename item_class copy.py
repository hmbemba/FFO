# 7.27.22
from dataclasses import dataclass, field
from typing import Any, List
from pathlib import Path
from . import errors
from typing import Union

@dataclass
class item:
    ''' 
-==================================================================-.
|Class Summary                                                       |
|====================================================================|

    A utility class that features basic functionality
    
    for getting basic path attributes (size, parent, etc) and 
    
    performing basic path functions (move, copy, delete, etc).
    
    
    # Inheritance
    
    If this class is inherited it has 3 attributes - location, size, name
    
    only location needs to be passed to constructor
    

-==================================================================-.
|Example Usage                                                       |
|====================================================================|

    see functions


-==================================================================-.
|Attributes                                                          |
|====================================================================|

    location
    size
    name
                                      

.-==================================================================-.
|Functions                                                           |
|====================================================================|
    
    FOLDER FUNCTIONS
    ---------------------------------
    item.FolderExists(path/to/file/or/folder)
    item.isFolder(path/to/file/or/folder)
    item.isFolderOrError(path/to/file/or/folder)
    
    FILE FUNCTIONS
    ---------------------------------------
    item.FileExists(path/to/file/or/folder)
    item.isFile(path/to/file/or/folder)
    item.isFileOrError(path/to/file/or/folder)
    
    UTIL FUNCTIONS
    -------------------------------------
    item.parent(path/to/file/or/folder)
    item.mkdir(path/to/file/or/folder)
    item.getSize(path/to/file/or/folder)
    
    item.move(path/to/file/or/folder) -> Need to implement
    item.copy(path/to/file/or/folder) -> Need to implement
    item.delSelf(path/to/file/or/folder) -> Need to implement
    '''

    def __init__(self, _path: Path):
        self.location = _path
        self.size = 0
        self.name = Path(_path).stem
    
    '''-----------------FOLDER FUNCTIONS---------------------'''

    @staticmethod
    def FolderExists(folderPath: Path) -> bool:
        return Path(folderPath).is_dir()
    
    '''Alias for semantic Reasons'''
    isFolder = FolderExists
    
    @staticmethod
    def isFolderOrError(_path: Path) -> Union[bool,errors.NotAFolderError]:
        if not item.isFolder(_path):
            raise errors.NotAFolderError(_path, "This is not a valid path to a folder")
        else:
            return item.isFolder(_path)
    
    
    '''-----------------FILE FUNCTIONS---------------------'''   
    @staticmethod
    def FileExists(filePath: Path) -> bool:
        return Path(filePath).is_file()

    '''Alias for semantic Reasons'''
    isFile = FileExists

    @staticmethod
    def isFileOrError(_path: Path) -> Union[bool,errors.NotAFileError]:
        if not item.isFile(_path):
            raise errors.NotAFileError(_path, "This is not a valid path to a file")
        else:
            return item.isFile(_path)
        
        
    '''-----------------UTIL FUNCTIONS---------------------'''
    
    @staticmethod
    def parent(path: Path) -> Path:
        return Path(path).parent
    
    @staticmethod
    def mkdir(dirName, inputPath: Path) -> None:
        if item.isFolder(inputPath):
            path = Path(inputPath) / dirName
            if item.FolderExists(path):
                raise errors.DirectoryAlreadyExistsError(path, "This directory already exists")
            else:
                Path.mkdir(path)
        
        if item.isFile(inputPath):
            path = item.parent(inputPath) / dirName
            if item.FolderExists(path):
                raise errors.DirectoryAlreadyExistsError(path, "This directory already exists")
            else:
                Path.mkdir(path)
    
    @staticmethod
    def getSize(_path: Path) -> dict:
        if item.isFolder(_path):
            sizeInBytes =  float( sum(f.stat().st_size for f in Path(_path).glob('**/*') if f.is_file()) )
            sizeInKb = sizeInBytes * 0.001
            sizeInMb = sizeInBytes * 0.000001
            sizeInGb = sizeInBytes * 0.000000001
            
            sizeDict = {
                'bytes':sizeInBytes,
                'kilobytes':sizeInKb,
                'megabytes':sizeInMb,
                'gigabytes':sizeInGb,
            }
            return sizeDict
        
        if item.isFile(_path):
            sizeInBytes =  float( Path(_path).stat().st_size )
            sizeInKb = sizeInBytes * 0.001
            sizeInMb = sizeInBytes * 0.000001
            sizeInGb = sizeInBytes * 0.000000001
            
            sizeDict = {
                'bytes':sizeInBytes,
                'kilobytes':sizeInKb,
                'megabytes':sizeInMb,
                'gigabytes':sizeInGb,
            }
            return sizeDict
            
    @staticmethod
    def move(src: Path, dst: Path) -> None:
        pass
    
    @staticmethod
    def copy(src: Path, dst: Path) -> None:
        pass
    
    def hasOneOfTheseSuffixes(pathEnding: str, suffixes: list[str]) -> bool:
        return {s.lower():True for s in suffixes}.get(pathEnding.lower(), False)
    
    def is_videoFile(pathEnding: str) -> bool:
        pathEnding = pathEnding.lower()
        allowedSuffixes = ['.mov', '.mp4', '.mpeg', '.mpg', '.flv']
        return {s.lower():True for s in allowedSuffixes}.get(pathEnding, False)
    
    def is_audioFile(pathEnding: str) -> bool:
        pathEnding = pathEnding.lower()
        allowedSuffixes = ['.mp3', '.wav', '.ogg', '.aac', '.flac']
        return {s.lower():True for s in allowedSuffixes}.get(pathEnding, False)

    def is_imageFile(pathSuffix: str) -> bool:
        pathSuffix = pathSuffix.lower()
        allowedSuffixes = ['.png', '.jpeg', 'tiff', '.jpg','.ping']
        return {s.lower():True for s in allowedSuffixes}.get(pathSuffix, False)

#print(hasOneOfTheseSuffixes('.mov',['.mp4', '.mov', ]))



