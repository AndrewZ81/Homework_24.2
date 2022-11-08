from marshmallow import Schema, fields


# Создаём класс сериализации сущностей "Запрос"
class RequestSchema(Schema):
    cmd_1 = fields.Str(required=True)
    value_1 = fields.Str(required=True)
    cmd_2 = fields.Str(required=True)
    value_2 = fields.Str(required=True)
    file_name = fields.Str(required=True)
