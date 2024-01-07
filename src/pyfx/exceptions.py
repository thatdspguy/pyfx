from typing import Optional


class KnobAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__()


class KnobDoesNotExistError(Exception):
    def __init__(self):
        super().__init__()


class FootswitchAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__()


class FootswitchDoesNotExistError(Exception):
    def __init__(self):
        super().__init__()


class PedalAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__()


class PedalDoesNotExistError(Exception):
    def __init__(self):
        super().__init__()


class PedalVariantDoesNotExistError(Exception):
    def __init__(self):
        super().__init__()


class InvalidRootPedalFolderError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)
