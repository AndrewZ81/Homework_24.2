from flask import Flask
from flask_restx import Api

from app.config import Config
from app.views.perform_query import queries_ns


def create_app(config_obj):
    """
    Создаёт экземпляр класса Flask и конфигурирует его
    :param config_obj: Объект конфигурации экземпляра класса Flask
    :return: Экземпляр класса Flask
    """
    application = Flask(__name__)
    application.config.from_object(config_obj)
    application.app_context().push()
    create_extensions(application)
    return application


def create_extensions(flask_app):
    """
    Создаёт расширения экземпляра класса Flask и конфигурирует их
    :param flask_app: Экземпляр класса Flask
    :return: None
    """
    api = Api(flask_app)
    api.add_namespace(queries_ns)


app_config = Config()
app = create_app(app_config)

if __name__ == "__main__":
    app.run()
