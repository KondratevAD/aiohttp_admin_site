from aiohttp_admin_site.exceptions import AdminException


__all__ = ['ValidationError', 'MapperError', ]


class ValidationError(AdminException):
    """This exception connected with wrong mapper form or some field."""


class MapperError(AdminException):
    """This exception connected with errors inside mapper class."""
