import json
from datetime import datetime

from backports.zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo
from Common.InfoType.QuarterInfo import QuarterInfo


class YearInfo(AbstractInfo):
    __header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _qi_1: QuarterInfo

    def __int__(self, dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._dt = dt
        self._qi_1 = QuarterInfo(dt - relativedelta(months=3))
        self._qi_2 = QuarterInfo(dt - relativedelta(months=6))
        self._qi_3 = QuarterInfo(dt - relativedelta(months=9))
        self._qi_4 = QuarterInfo(dt - relativedelta(months=12))

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "start": str(self._qi_1.StopDateTime),
            "stop": str(self._qi_4.StartDateTime)
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
