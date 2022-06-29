import json
import math
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from backports.zoneinfo import ZoneInfo
from fiscalyear import FiscalDateTime, FiscalQuarter, FiscalYear, FiscalMonth, FiscalDay, FiscalDate
from prettytable import PrettyTable
from typing import List

from Common.InfoType.AbstractInfo import AbstractInfo
from Common.InfoType.QuarterInfo import QuarterInfo


class YearInfo(AbstractInfo):

    __header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _qi_list: List[QuarterInfo] = []

    def __int__(self, dt: datetime):
        self._dt = dt
        l: List[QuarterInfo] = []
        l.append(QuarterInfo(dt - relativedelta(months=3)))
        l.append(QuarterInfo(dt - relativedelta(months=6)))
        l.append(QuarterInfo(dt - relativedelta(months=9)))
        l.append(QuarterInfo(dt - relativedelta(months=12)))
        self._qi_list = l

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        self._pretty_table.add_row(['Length', len(self._qi_list)])
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "len": len(self._qi_list)
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
