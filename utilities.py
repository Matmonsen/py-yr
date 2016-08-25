# -*- coding: utf-8 -*-

from _datetime import datetime


def parse_iso8601(time: str) -> datetime:
    """
    Parses iso8601 to datetime
    Args:
        time(str): string iso8601 formatted

    Returns(datetime): datetime representation of iso8601 date

    """
    try:
        data = datetime.strptime(time, '%Y-%m-%dT%X')
    except ValueError:
        try:
            data = datetime.strptime(time, '%Y-%m-%d')
        except ValueError:
            try:
                data = datetime.strptime(time, '%Y-%m-%d%XZ')
            except ValueError:
                data = time
    return data
