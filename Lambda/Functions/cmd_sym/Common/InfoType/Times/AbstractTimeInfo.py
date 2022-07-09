from datetime import datetime

from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class AbstractTimeInfo(AbstractInfo):
    _stop_dt: datetime = datetime.now()
    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()

    @property
    def stop_datetime(self) -> datetime:
        return self._stop_dt

    @property
    def current_datetime(self) -> datetime:
        return self._stop_dt
