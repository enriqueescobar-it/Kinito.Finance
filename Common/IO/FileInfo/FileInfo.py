from Common.IO.FileInfo import IFileInfo
from pathlib import Path
import os
import datetime


class FileInfo(IFileInfo):
    _path_orig: str = ''
    _path_abs: str = ''
    _dir_name: str = ''
    _dir_path: str = ''
    _extension: str = ''
    _name: str = ''
    _is_abs: bool = False
    _exists: bool = False

    def __init__(self, file_name: str = ''):
        self._path_orig = file_name
        self._exists = Path(self._path_orig).exists()
        if self._exists:
            self._is_abs = Path(self._path_orig).is_absolute()
            self._path_abs = Path(self._path_orig).resolve()
            self._dir_name = Path(self._path_orig).parent
            self._dir_path = Path(self._path_orig).resolve().parent
            self._extension = Path(self._path_orig).suffix
            self._name = Path(self._path_orig).stem
            self._stats = os.stat(self._path_abs)

    @property
    def Dir(self):
        return self._dir_path

    @property
    def DirName(self):
        return self._dir_name

    @property
    def Exists(self):
        return self._exists

    @property
    def Extension(self):
        return self._extension

    @property
    def FullPath(self):
        return self._path_abs

    @property
    def OriginalPath(self):
        return self._path_orig

    @property
    def IsAbsolute(self):
        return self._is_abs

    @property
    def IsReadOnly(self):
        return os.access(self._path_abs, os.R_OK)

    @property
    def LastAccessTime(self):
        return datetime.datetime.fromtimestamp(self._stats.st_ctime)

    @property
    def LastWriteTime(self):
        return datetime.datetime.fromtimestamp(self._stats.st_mtime)

    @property
    def Length(self):
        return self._stats.st_size

    @property
    def Name(self):
        return self._name
