from rtamt.exception.exception import RTAMTException

class LTLException(RTAMTException):
    pass

class LTLPastifyException(LTLException):
    pass

class LTLParseException(LTLException):
    pass

class LTLOfflineException(LTLException):
    pass

class LTLSpecificationException(LTLException):
    pass

class LTLNotImplementedException(LTLException):
    pass