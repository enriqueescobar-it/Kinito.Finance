from abc import abstractmethod

from Common.Objects.Interfaceable import Interfaceable


class IFileInfo(Interfaceable):

    @abstractmethod
    def AppendText(self) -> bool:
        pass

    @abstractmethod
    def CopyTo(self) -> bool:
        pass

    @abstractmethod
    def Create(self) -> bool:
        pass

    @abstractmethod
    def CreateText(self) -> bool:
        pass

    @abstractmethod
    def Decrypt(self):
        pass

    @abstractmethod
    def Delete(self):
        pass

    @abstractmethod
    def Encrypt(self):
        pass

    @abstractmethod
    def MoveTo(self):
        pass

    @abstractmethod
    def Open(self):
        pass

    @abstractmethod
    def OpenRead(self):
        pass

    @abstractmethod
    def OpenText(self):
        pass

    @abstractmethod
    def OpenWrite(self):
        pass

    @abstractmethod
    def Replace(self):
        pass

    @property
    @abstractmethod
    def Dir(self):
        pass

    @property
    @abstractmethod
    def DirName(self):
        pass

    @property
    @abstractmethod
    def Exists(self):
        pass

    @property
    @abstractmethod
    def Extension(self):
        pass

    @property
    @abstractmethod
    def FullName(self):
        pass

    @property
    @abstractmethod
    def FullPath(self):
        pass

    @property
    @abstractmethod
    def OriginalPath(self):
        pass

    @property
    @abstractmethod
    def IsAbsolute(self):
        pass

    @property
    @abstractmethod
    def IsReadOnly(self):
        pass

    @property
    @abstractmethod
    def LastAccessTime(self):
        pass

    @property
    @abstractmethod
    def LastWriteTime(self):
        pass

    @property
    @abstractmethod
    def Length(self):
        pass

    @property
    @abstractmethod
    def Name(self):
        pass
