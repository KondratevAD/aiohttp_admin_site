from aiohttp_admin_site.mappers.exceptions import ValidationError


def integer(*, max_value: int = None, min_value: int = None):
    """
    This validator need to restrict value in field.

        from aiohttp_admin_site.mappers import Mapper, IntField

        class Foo(Mapper):
            field_name = IntField(validators=[integer(max_value=5)])
    """
    def integer_validator(value) -> None:
        if value and max_value is not None and value > max_value:
            raise ValidationError(
                f"'{value}' cannot be greater than {max_value}"
            )
        if value and min_value is not None and value < min_value:
            raise ValidationError(
                f"'{value}' cannot be less than {min_value}"
            )
    return integer_validator
