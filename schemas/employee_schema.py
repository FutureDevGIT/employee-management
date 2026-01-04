from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    department = fields.Str(required=True, validate=validate.Length(min=1))
    salary = fields.Int(required=True)
