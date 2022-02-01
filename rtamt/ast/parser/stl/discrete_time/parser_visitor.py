from decimal import Decimal
from fractions import Fraction

from rtamt.ast.parser.stl.parser_visitor import StlAstParserVisitor
from rtamt.exception.stl.exception import STLParseException

class StlDiscreteTimeAstParserVisitor(StlAstParserVisitor):

    def visitIntervalTimeLiteral(self, ctx):
        text = ctx.literal().getText()
        out = Fraction(Decimal(text))

        if ctx.unit() == None:
            # default time unit is seconds - conversion of the bound to ps
            unit = self.spec.unit
        else:
            unit = ctx.unit().getText()

        out = out * self.spec.U[unit]

        sp = Fraction(self.spec.get_sampling_period())

        out = out / sp

        if out.numerator % out.denominator > 0:
            raise STLParseException('The STL operator bound must be a multiple of the sampling period')

        out = int(out / self.spec.sampling_period)

        return out