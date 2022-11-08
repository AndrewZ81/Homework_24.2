from app.functions import filter_query, map_query, unique_query, sort_query, limit_query, filter_by_regex_query

# Создаём словарь для выбора функции в зависимости от строки команды
CMDS_TO_EXECUTE = {
    "filter": filter_query,
    "filter_by_regex": filter_by_regex_query,
    "map": map_query,
    "unique": unique_query,
    "sort": sort_query,
    "limit": limit_query
}
