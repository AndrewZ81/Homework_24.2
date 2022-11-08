from flask import request
from constants import CMDS_TO_EXECUTE
from typing import Iterator, Optional


def iterate_file(file_with_logs) -> Iterator:
    with open(file_with_logs) as file:
        for i in file:
            yield i


def create_query(cmd_1: str="", value_1:str ="", cmd_2: str="", value_2: str="") -> list:
    file_name = request.json["file_name"]
    generator: Iterator = iterate_file(file_name)
    result_1: list = CMDS_TO_EXECUTE[cmd_1](generator, value_1)
    result_2: list = CMDS_TO_EXECUTE[cmd_2](result_1, value_2)
    return result_2
