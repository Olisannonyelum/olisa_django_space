from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError


valid_unit_measurements = ['pounds', 'lbs', 'oz', 'gram']

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg(value)# what this does is that it take in unit an chack if the unit is valid if not it will raise an error which will be capture as shown
        print('this is whare  we have.......>', 4.5*single_unit)
    except UndefinedUnitError as e:
        raise ValidationError(f"{value} is not a valid unit of measure")
    except:
        raise ValidationError(f"{value} is invalid. Unknown error.")

    """
    what the above line of code does is that make sure that the unit inserted in the 
    unit field is a valid unit
    """
      
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f"{value} is not a valid unit of measure")