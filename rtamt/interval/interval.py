import logging

class Interval(object):
    """A class for storing integer intervals

        Attributes
        --------------
        begin : int
            beginning of the interval
        end : int
            end of the interval

        Methods
        --------------
        begin, end
            Getter for begin and end
            The object is immutable - the setter issues a warning message and does nothing
        """
    def __init__(self, begin, end):
        """Constructor for Interval
        Parameters:
            begin : int
                Beginning of the interval
            end : int
                End of the interval
        """
        self.begin = begin
        self.end = end

    @property
    def begin(self):
        """Getter for begin"""
        return self.__begin

    @begin.setter
    def begin(self, begin):
        self.__begin = begin

    @property
    def end(self):
        """Getter for end"""
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end