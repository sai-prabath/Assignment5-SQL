
class EventNotFoundException(Exception):
    def __init__(self, message="Event not found."):
        super().__init__(message)

class InvalidBookingIDException(Exception):
    def __init__(self, message="Invalid booking ID."):
        super().__init__(message)

class DatabaseOperationException(Exception):
    def __init__(self, message="Database operation failed."):
        super().__init__(message)

class ProcessLookupError(Exception):
    def __init__(self, message="Process lookup error."):
        super().__init__(message)

class NullPointerExcpetion(Exception):
    def __init__(self, message="Null pointer exception."):
        super().__init__(message)
