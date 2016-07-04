from marshmallow_sqlalchemy import ModelSchema
from userv.encyclopedia.models import Fact


class FactSchema(ModelSchema):
    class Meta:
        model = Fact

fact_schema = FactSchema()
