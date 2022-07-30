from marshmallow import EXCLUDE, Schema, fields, pre_load


class ResultSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    download = fields.Float()
    upload = fields.Float()
    ping = fields.Float()
    timestamp = fields.DateTime()
