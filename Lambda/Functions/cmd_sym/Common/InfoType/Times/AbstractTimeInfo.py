from datetime import datetime

from Common.InfoType.AbstractInfo import AbstractInfo


class AbstractTimeInfo(AbstractInfo):
    _stop_dt: datetime = datetime.now()

    @property
    def stop_datetime(self) -> datetime:
        return self._stop_dt
