import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

def validate_unit(value):
    ureg = pint.UnitRegistry()
    try:
        Unit = ureg[value]
    
    except UndefinedUnitError as e:
        raise ValidationError(f'{value} is not a valid unit')