from Common.IO.FileInfo import IFileInfo
from pathlib import Path


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
        self._path_abs = Path(self._path_orig).resolve()
        self._is_abs = Path(self._path_orig).is_absolute()
        self._exists = Path(self._path_orig).exists()
        self._dir_name = Path(self._path_orig).parent
        self._dir_path = Path(self._path_orig).resolve().parent
        self._extension = Path(self._path_orig).suffix
        self._name = Path(self._path_orig).stem

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
        pass

    @property
    def LastAccessTime(self):
        pass

    @property
    def LastWriteTime(self):
        pass

    @property
    def Length(self):
        pass

    @property
    def Name(self):
        return self._name
