from flask_marshmallow import Marshmallow
from .models import Fact

ma = Marshmallow()

class FactSchema(ma.ModelSchema):
    class Meta:
        model = Fact
    

