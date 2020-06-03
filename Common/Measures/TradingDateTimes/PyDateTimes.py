import datetime


def DateTimeNow():
    return datetime.date.today()


def DateTime1WeekAgo():
    return DateTimeNow() - datetime.timedelta(7+1)


def DateTime2WeekAgo():
    return DateTimeNow() - datetime.timedelta(14+1)


def DateTime4WeekAgo():
    return DateTimeNow() - datetime.timedelta(28+1)


def DateTime26WeekAgo():
    return DateTimeNow() - datetime.timedelta(182+1)


def DateTime52WeekAgo():
    return DateTimeNow() - datetime.timedelta(365+1)


def DateTimeWeeksAgo(n=0):
    return DateTimeNow() - datetime.timedelta(7*n+1)
