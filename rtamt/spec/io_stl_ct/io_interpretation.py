from enum import Enum

class IOInterpretation(Enum):
    STANDARD = 'standard'
    OUTPUT_ROBUSTNESS = 'output-robustness'
    INPUT_VACUITY = 'input-vacuity'
    INPUT_ROBUSTNESS = 'input-robustness'
    OUTPUT_VACUITY = 'output-vacuity'

    def __str__(self):
        return self.value
