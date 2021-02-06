#from Common.IO.DirInfo.IDirInfo import IDirInfo
from abc import *
from pathlib import Path
import os
import datetime


class DirInfo(ABC):
    __length: int = 0
    __path_orig: str = ''
    __path_abs: str = ''
    __dir_name: str = ''
    __dir_path: str = ''
    __dir_root: str = ''
    __name: str = ''
    __is_abs: bool = False
    __exists: bool = False
    __is_dir: bool = False
    __a_time: datetime = datetime.datetime.now()
    __c_time: datetime = datetime.datetime.now()
    __m_time: datetime = datetime.datetime.now()

    def __init__(self, dir_name: str):
        self.__path_orig = dir_name
        self.__exists = Path(self.__path_orig).exists()
        self.__is_dir = Path(self.__path_orig).is_dir()
        if self.__exists and self.__is_dir:
            self.__is_abs = Path(self.__path_orig).is_absolute()
            self.__path_abs = Path(self.__path_orig).resolve()
            self.__dir_name = Path(self.__path_abs).name
            self.__dir_path = Path(self.__path_abs).resolve().parent
            self.__dir_root = Path(self.__path_abs).anchor
            self.__name = Path(self.__path_abs).stem
            self.__stats = os.stat(self.__path_abs)
            self.__a_time = datetime.datetime.fromtimestamp(self.__stats.st_atime)
            self.__c_time = datetime.datetime.fromtimestamp(self.__stats.st_ctime)
            self.__m_time = datetime.datetime.fromtimestamp(self.__stats.st_mtime)
            self.__length = self.__stats.st_size
            print(self.__stats.st_mode)

    def __str__(self):
        return self.__path_abs

    def CopyTo(self, new_path: str) -> bool:
        return False

    def Create(self) -> bool:
        return False

    def Delete(self) -> bool:
        return False

    def MoveTo(self, new_path: str) -> bool:
        return False

    @property
    def DirPath(self):
        return self.__dir_path

    @property
    def DirName(self):
        return self.__dir_name

    @property
    def Exists(self):
        return self.__exists

    @property
    def Root(self):
        return self.__dir_root

    @property
    def FullPath(self):
        return self.__path_abs

    @property
    def IsAbsolute(self):
        return self.__is_abs

    @property
    def IsReadOnly(self):
        return os.access(self.__path_abs, os.R_OK)

    @property
    def LastAccessTime(self):
        return self.__a_time

    @property
    def CreationTime(self):
        return self.__c_time

    @property
    def LastWriteTime(self):
        return self.__m_time

    @property
    def Length(self):
        return self.__length

    @property
    def Name(self):
        return self.__name

    @property
    def OriginalPath(self):
        return self.__path_orig
