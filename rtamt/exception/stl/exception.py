from rtamt.exception.exception import RTAMTException

class STLException(RTAMTException):
    pass

class STLParseException(STLException):
    pass

class STLOfflineException(STLException):
    pass

class STLSpecificationException(STLException):
    pass

class STLNotImplementedException(STLException):
    pass