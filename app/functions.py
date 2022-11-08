import re


def check_regex_incoming(data, regex=""):
    regex_for_searching = re.compile(rf"{regex}")
    searching_result = regex_for_searching.search(data)
    if searching_result is None:
        return False
    return True


def filter_query(data, param=""):
    return list(filter(lambda x: param in x, data))


def filter_by_regex_query(data, param=""):
    return list(filter(lambda x: check_regex_incoming(x, param), data))


def map_query(data, param=""):
    column_number = int(param)
    return list(map(lambda x: x.split(" ")[column_number], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def sort_query(data, param=""):
    return sorted(list(data), reverse=param == "desc")


def limit_query(data, param=""):
    limit_number = int(param)
    return list(data)[:limit_number]
