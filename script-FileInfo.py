from Common.IO.FileInfo.FileInfo import FileInfo
from Common.IO.DirInfo.DirInfo import DirInfo


fi: FileInfo = FileInfo(file_name='F:\Disk_X\Kinito.Finance\README.txt')
#fi: DirInfo = DirInfo(dir_name='Common')
print('Dir', fi.DirPath)
print('DirName', fi.DirName)
print('Name', fi.Name)
print(fi.Exists)
print('FullPath', fi.FullPath)
print('OriginalPath', fi.OriginalPath)
print('Root', fi.Root)
print(fi.IsAbsolute)
print(fi.IsReadOnly)
print(fi.LastAccessTime)
print(fi.CreationTime)
print(fi.LastWriteTime)
print(fi.Length)
print(fi.Extension)
print(fi.Create())
