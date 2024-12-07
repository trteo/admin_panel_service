from django.db import models


class Cart:
    """
    id: int

    items: List[FK(int)]
    user id: FK(int)
    """
    ...


class Orders:
    """
    id: int

    items: List[FK(int)]
    user id: FK(int)
    delivery address: str
    sum price: float
    is paid: bool

    date_created: bool
    """
    ...
