from rest_framework.serializers import ValidationError


def validate_hierarchy(data):
    """Валидация иерархии объекта Vendor."""
    level = dict(data).get("level")
    supplier = dict(data).get("supplier")
    if level > 0 and supplier is None:
        raise ValidationError(
            "При уровне больше 0 требуется указать поставщика."
        )
    elif supplier is not None and level <= supplier.level:
        raise ValidationError(
            "Поставщик не может быть ниже или равен в иерархии"
        )
    return data
