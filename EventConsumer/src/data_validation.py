# Created by Aurimas A. Nausedas on 07/24/22.
# Updated by Aurimas A. Nausedas on 07/25/22.
# Updated by Aurimas A. Nausedas on 07/26/22.


from marshmallow import Schema, fields

class Event(Schema):
    event_type = fields.Str(required=True)
    event_payload = fields.Str(required=True)
