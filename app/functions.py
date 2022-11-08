def filter_query(data, param=""):
    return list(filter(lambda x: param in x, data))


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
