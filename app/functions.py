import re
from re import Match
from typing import Pattern, Optional, Iterator


def check_regex_incoming(data, regex="") -> bool:
    regex_for_searching: Pattern = re.compile(rf"{regex}")
    searching_result: Optional[Match] = regex_for_searching.search(data)
    if searching_result is None:
        return False
    return True


def filter_query(data: Iterator, param: str="") -> list:
    return list(filter(lambda x: param in x, data))


def filter_by_regex_query(data: Iterator, param: str="") -> list:
    return list(filter(lambda x: check_regex_incoming(x, param), data))


def map_query(data: Iterator, param: str="") -> list:
    column_number: int = int(param)
    return list(map(lambda x: x.split(" ")[column_number], data))


def unique_query(data: Iterator, *args, **kwargs) -> list:
    return list(set(data))


def sort_query(data: Iterator, param: str="") -> list:
    return sorted(list(data), reverse=param == "desc")


def limit_query(data: Iterator, param: str="") -> list:
    limit_number: int = int(param)
    return list(data)[:limit_number]
