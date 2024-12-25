class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(self, messege='Введено значение за границами игрового поля!'):
        super().__init__(messege)


class CellOccupiedError(Exception):
    """Выбрасывается, если выбрано значение уже занято."""

    def __init__(self, message='Попытка изменить занятую ячейку'):
        super().__init__(message)
