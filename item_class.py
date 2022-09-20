# 7.27.22
from dataclasses import dataclass, field
from typing import Any, List
from pathlib import Path
from . import errors
from typing import Union
import pprint

@dataclass
class item:
    path: str

    def __post_init__(self):
        self.name = Path(self.path).stem
    
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
    
    '''Alias for semantic Reasons'''
    FolderExistsOrError = isFolderOrError
    
    
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
    
    '''Alias for semantic Reasons'''
    FileExistsOrError = isFileOrError
        
        
    '''-----------------UTIL FUNCTIONS---------------------'''
    
    @staticmethod
    def parent(path: Path) -> Path:
        return Path(path).parent
    
    @staticmethod
    def mkdir(dirName:str, dst: Path) -> None:
        if item.isFolder(dst):
            path = Path(dst) / dirName
            if item.FolderExists(path):
                raise errors.DirectoryAlreadyExistsError(path, "This directory already exists")
            else:
                Path.mkdir(path)
        
        if item.isFile(dst):
            path = item.parent(dst) / dirName
            if item.FolderExists(path):
                raise errors.DirectoryAlreadyExistsError(path, "This directory already exists")
            else:
                Path.mkdir(path)
    
    @staticmethod
    def mkfileOverwrite(fileNameWithExt:str, dst: Path, content:str = '') -> None:
        '''
        Creates a new file if it doesn't exist
        Overwrites it if it does
        '''
        path = f"{dst}\\{fileNameWithExt}"
        with open(path, 'w') as f:
            f.write(content)

    @staticmethod
    def mkfileNoOverwrite(fileNameWithExt:str, dst: Path, content:str = '') -> None:
        '''
        Creates a new file, UNLESS that file already exists then it will raise an error
        '''
        path = f"{dst}\\{fileNameWithExt}"
        if item.FileExists(path):
            raise Exception("This file already exists. To overwrite it use mkfileOverwrite")
        else:
            with open(path, 'w') as f:
                f.write(content)
    
    @staticmethod
    def getSize(_path: Path) -> dict:
        '''
        Gets the size of a file or folder
        '''
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
        '''
        item.hasOneOfTheseSuffixes(pathEnding=Path(file).suffix,suffixes=['.pdf'])
        '''
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





