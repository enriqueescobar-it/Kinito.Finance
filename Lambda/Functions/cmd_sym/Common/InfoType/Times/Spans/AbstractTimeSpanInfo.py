from datetime import datetime

from prettytable import PrettyTable

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo


class AbstractTimeSpanInfo(AbstractTimeInfo):
    _start_dt: datetime = datetime.now()
    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()

    @property
    def start_datetime(self) -> datetime:
        return self._start_dt
