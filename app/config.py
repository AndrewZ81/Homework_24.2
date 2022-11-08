# Создаём класс конфигурации приложения
from typing import Dict


class Config(object):
    RESTX_JSON: Dict[str, bool] = {"ensure_ascii": False}
    DEBUG: bool = True
