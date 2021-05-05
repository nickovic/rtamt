

class Node(object):
    """A class for storing STL nodes
    Attributes
    --------------
    horizon : int
        integer denoting how much in the future the underlying formula must look

    Methods
    --------------
    horizon
        Getter and setter for horizon
    """

    def __init__(self):
        self.evaluator = None #TODO: Tom do not know why the semantics side is needed in node.
        self.node = None

        """Constructor for Node"""
        self.horizon = 0 #TODO: Tom thinks horizon needs only timed autokmaton.
        self.in_vars = []
        self.out_vars = []
        self.children = list()
        self.name = ''

    def addChild(self, child):
        self.children.append(child)

    def accept(self, visitor):
        """accept: recursive function needed to implement node visitors
        Inputs:
        visitor - Visitor object
        """
        for child in self.children:
            child.accept(visitor)

    @property
    def horizon(self):
        """Getter for the horizon"""
        return self.__horizon

    @horizon.setter
    def horizon(self, horizon):
        """Setter for the horizon"""
        self.__horizon = horizon

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children

    @property
    def in_vars(self):
        """Getter for the in_vars"""
        return self.__in_vars

    @in_vars.setter
    def in_vars(self, in_vars):
        """Setter for the in_vars"""
        self.__in_vars = in_vars

    @property
    def out_vars(self):
        """Getter for the out_vars"""
        return self.__out_vars

    @out_vars.setter
    def out_vars(self, out_vars):
        """Setter for the out_vars"""
        self.__out_vars = out_vars

    def add_child(self, child):
        self.children.append(child)

    def accept(self, visitor):
        """accept: recursive function needed to implement node visitors
        Inputs:
        visitor - Visitor object
        """
        for child in self.children:
            child.accept(visitor)

    @property
    def name(self):
        """Getter for the name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Setter for the name"""
        self.__name = name

    def __repr__(self):
        '''Returns representation of the object'''
        return self.__class__.__name__

    @property
    def node(self):
        """Getter for the node"""
        return self.__node

    @node.setter
    def node(self, node):
        """Setter for the horizon"""
        self.__node = node

    def __repr__(self):
        '''Returns representation of the object'''
        return self.__class__.__name__

    @property
    def evaluator(self): #TODO: Tom thinks perhaps we can separete evaluator or operator.
        """Getter for the online_evaluator"""
        return self.__evaluator

    @evaluator.setter
    def evaluator(self, evaluator): #TODO: Tom thinks perhaps we can separete evaluator or operator.
        """Setter for the online_evaluator"""
        self.__evaluator = evaluator
