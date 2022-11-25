from aiohttp_admin_site.exceptions import AdminException


__all__ = ["PermissionDenied", ]


class PermissionDenied(AdminException):
    """If has not access for some operation."""
