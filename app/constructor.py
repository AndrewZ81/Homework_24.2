from flask import request
from constants import CMDS_TO_EXECUTE


def iterate_file(file_with_logs):
    with open(file_with_logs) as file:
        for i in file:
            yield i


def create_query(cmd_1="", value_1="", cmd_2="", value_2=""):
    file_name: str = request.json["file_name"]
    generator = iterate_file(file_name)
    result_1 = CMDS_TO_EXECUTE[cmd_1](generator, value_1)
    result_2 = CMDS_TO_EXECUTE[cmd_2](result_1, value_2)
    return result_2
