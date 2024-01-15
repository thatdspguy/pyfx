from typing import Optional

"""Knob Errors"""


class KnobAlreadyExistsError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class KnobDoesNotExistError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class KnobRangeError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class KnobPrecisionError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class KnobModeError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class KnobNameError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


"""Footswitch Errors"""


class FootswitchAlreadyExistsError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class FootswitchDoesNotExistError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


"""Pedal Errors"""


class PedalAlreadyExistsError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class PedalDoesNotExistError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class PedalVariantDoesNotExistError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


class InvalidRootPedalFolderError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


"""Audio Errors"""


class AudioOutputDeviceNotFoundError(Exception):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)
