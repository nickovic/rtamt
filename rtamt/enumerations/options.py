from enum import Enum

class Semantics(Enum):
    STANDARD = "standard"
    OUTPUT_ROBUSTNESS = "output-robustness"
    INPUT_VACUITY = "input-vacuity"
    INPUT_ROBUSTNESS = "input-robustness"
    OUTPUT_VACUITY = "output-vacuity"

    def __str__(self):
        return self.value

class Language(Enum):
    PYTHON = "python"
    CPP = "C++"
    def __str__(self):
        return self.value

class TimeInterpretation(Enum):
    DISCRETE = "discrete_time"
    DENSE = "dense-time"
    def __str__(self):
        return self.value


class TemporalLogic(Enum):
    LTL = "ltl",
    STL = "stl"

    def __str__(self):
        return self.value

class Mode(Enum):
    ONLINE = "online",
    OFFLINE = "offline"
    def __str__(self):
        return self.value