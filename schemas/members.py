from marshmallow import Schema, fields


class MembersSchema(Schema):
    
    member_id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    date_of_birth = fields.Date(required=True)
    active = fields.String(required=True)  
    


 