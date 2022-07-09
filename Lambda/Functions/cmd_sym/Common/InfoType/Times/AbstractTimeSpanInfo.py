from datetime import datetime

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo


class AbstractTimeSpanInfo(AbstractTimeInfo):
    _start_dt: datetime = datetime.now()

    @property
    def start_datetime(self) -> datetime:
        return self._start_dt
