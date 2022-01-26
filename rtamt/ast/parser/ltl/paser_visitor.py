
import logging
import operator

from antlr4 import *

from rtamt.parser.ltl.LtlParserVisitor import LtlParserVisitor

from rtamt.node.ltl.variable import Variable
from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.previous import Previous
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.until import Until
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.xor import Xor
from rtamt.node.ltl.always import Always
from rtamt.node.ltl.eventually import Eventually
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.since import Since
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.constant import Constant

from rtamt.exception.stl.exception import STLParseException


class LtlAstParserVisitor(LtlParserVisitor):

    def __init__(self, const_val_dict, var_subspec_dict, var_type_dict, var_io_dict, comp_op_mod, var_object_dict):
        super(LtlAstParserVisitor, self).__init__()
        self.const_val_dict = const_val_dict
        self.var_subspec_dict = var_subspec_dict
        self.var_type_dict = var_type_dict
        self.var_io_dict = var_io_dict
        self.comp_op_mod = comp_op_mod
        self.var_object_dict = var_object_dict

    #TODO Ton is not confidence this location.
    def create_var_from_name(self, var_name):
        var = None
        var_type = self.var_type_dict[var_name]
        if var_type.encode('utf-8') == 'float'.encode('utf-8'):
            var = float()
        elif var_type.encode('utf-8') == 'int'.encode('utf-8'):
            var = int()
        elif var_type.encode('utf-8') == 'complex'.encode('utf-8'):
            var = complex()
        else:
            try:
                var_module = self.modules[var_type]
                class_ = getattr(var_module, var_type)
                var = class_()
            except KeyError:
                raise STLParseException('The type {} does not seem to be imported.'.format(var_type))
        return var

    def visitExprPredicate(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        op_type = self.str_to_op_type(ctx.comparisonOp().getText())
        node = Predicate(child1, child2, op_type)

        node.horizon = int(0)
        return node

    def visitExprId(self, ctx):
        id = ctx.Identifier().getText();

        # Identifier is a constant
        if id in self.const_val_dict:
            val = self.const_val_dict[id]
            node = Constant(float(val))
        # Identifier is either an input variable or a sub-formula
        elif id in self.var_subspec_dict:
                node = self.var_subspec_dict[id]
                return node
        else:
            id_tokens = id.split('.')
            id_head = id_tokens[0]
            id_tokens.pop(0)
            id_tail = '.'.join(id_tokens)

            try:
                var = self.create_var_from_name(id_head)
                if (not id_tail):
                    if (not isinstance(var, (int, float))):
                        raise STLParseException('Variable {} is not of type int or float'.format(id))
                else:
                    try:
                        value = operator.attrgetter(id_tail)(var)
                        if (not isinstance(value, (int, float))):
                            raise STLParseException(
                                'The field {0} of the variable {1} is not of type int or float'.format(id, id_head))
                    except AttributeError as err:
                        raise STLParseException(err)
            except KeyError:
                if id_tail:
                    raise STLParseException('{0} refers to undeclared variable {1} of unknown type'.format(id, id_head))
                else:
                    var = float()
                    self.var_object_dict[id] = var
                    self.spec.add_var(id)
                    logging.warning('The variable {} is not explicitely declared. It is implicitely declared as a '
                                'variable of type float'.format(id))

            var_io = self.var_io_dict[id_head]
            node = Variable(id_head, id_tail, var_io)

        node.horizon = int(0)
        return node


    def visitVariableDeclaration(self, ctx):
        # fetch the variable name, type and io signature
        var_name = ctx.Identifier().getText()
        var_type = ctx.domainType().getText()

        self.spec.declare_var(var_name, var_type)
        self.spec.var_io_dict[var_name] = 'output'

        # If 'var' is input, add to the set of input vars
        # If 'var' is output, add to the set of output vars
        if (not ctx.ioType() is None):
            if (not ctx.ioType().Input() is None):
                var_iotype = 'input'
            elif (not ctx.ioType().Output() is None):
                var_iotype = 'output'
        self.spec.set_var_io_type(var_name, var_iotype)

        self.visitChildren(ctx)

    def visitConstantDeclaration(self, ctx):
        # fetch the variable name, type and io signature
        const_name = ctx.identifier().getText()
        const_type = ctx.domainType().getText()
        const_value = ctx.literal().getText()

        self.spec.declare_const(const_name, const_type, const_value)

        self.spec.visitChildren(ctx)

    def visitRosTopic(self, ctx):
        var_name = ctx.Identifier(0).getText()
        topic_name = ctx.Identifier(1).getText()
        self.spec.set_var_topic(var_name, topic_name)

    def visitModImport(self, ctx):
        module_name = ctx.Identifier(0).getText()
        var_type = ctx.Identifier(1).getText()
        self.spec.import_module(module_name, var_type)

    def visitExprAddition(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Addition(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprSubtraction(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Subtraction(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprMultiplication(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Multiplication(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprDivision(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Division(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprAbs(self, ctx):
        child = self.visit(ctx.real_expression())
        node = Abs(child)
        node.horizon = child.horizon
        return node

    def visitExprSqrt(self, ctx):
        child = self.visit(ctx.real_expression())
        node = Sqrt(child)
        node.horizon = child.horizon
        return node

    def visitExprExp(self, ctx):
        child = self.visit(ctx.real_expression())
        node = Exp(child)
        node.horizon = child.horizon
        return node

    def visitExprPow(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Pow(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprNot(self, ctx):
        child = self.visit(ctx.expression())
        node = Neg(child)
        node.horizon = child.horizon
        return node

    def visitExprRise(self, ctx):
        child = self.visit(ctx.expression())
        node = Rise(child)
        node.horizon = child.horizon
        return node

    def visitExprLiteral(self, ctx):
        val = float(ctx.literal().getText())
        node = Constant(val)
        node.horizon = 0
        return node

    def visitExprFall(self, ctx):
        child = self.visit(ctx.expression())
        node = Fall(child)
        node.horizon = child.horizon
        return node

    def visitExprAnd(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Conjunction(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprOr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Disjunction(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprImplies(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Implies(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprIff(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Iff(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprXor(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Xor(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprAlways(self, ctx):
        child = self.visit(ctx.expression())
        horizon = child.horizon
        node = Always(child)
        node.horizon = horizon
        return node

    def visitExprEv(self, ctx):
        child = self.visit(ctx.expression())
        node = Eventually(child)
        return node

    def visitExprPrevious(self, ctx):
        child = self.visit(ctx.expression())
        node = Previous(child)
        node.horizon = child.horizon
        return node

    def visitExprNext(self, ctx):
        child = self.visit(ctx.expression())
        node = Next(child)
        node.horizon = child.horizon + 1
        return node

    def visitExpreOnce(self, ctx):
        child = self.visit(ctx.expression())
        node = Once(child)
        node.horizon = child.horizon
        return node

    def visitExprHist(self, ctx):
        child = self.visit(ctx.expression())
        node = Historically(child)
        node.horizon = child.horizon
        return node

    def visitExprSince(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Since(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprUntil(self, ctx):
        # Parse children
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))

        node = Until(child1, child2)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprUnless(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())

        left = Always(child1, 0, interval.end)
        right = Until(child1, child2)
        node = Disjunction(left, right)

        node.horizon = max(child1.horizon, child2.horizon) + interval.end
        return node

    def visitExprParen(self, ctx):
        return self.visit(ctx.expression())

    def visitExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitAssertion(self, ctx):
        out = self.visit(ctx.expression())

        implicit = False
        if not ctx.Identifier():
            id = 'out'
            implicit = True
        else:
            id = ctx.Identifier().getText();

        self.var_subspec_dict[id] = out
        id_tokens = id.split('.')
        id_head = id_tokens[0]
        id_tokens.pop(0)
        id_tail = '.'.join(id_tokens)

        try:
            #var = self.spec.var_object_dict[id_head]
            var = self.create_var_from_name(id_head)
            if (not id_tail):
                if (not isinstance(var, (int, float))):
                    raise STLParseException('Variable {} is not of type int or float'.format(id))
            else:
                try:
                    value = operator.attrgetter(id_tail)(var)
                    if (not isinstance(value, (int, float))):
                        raise STLParseException(
                            'The field {0} of the variable {1} is not of type int or float'.format(id, id_head))
                except AttributeError as err:
                    raise STLParseException(err)
        except KeyError:
            if id_tail:
                raise STLParseException('{0} refers to undeclared variable {1} of unknown type'.format(id, id_head))
            else:
                var = float()
                self.var_object_dict[id] = var
                self.spec.add_var(id)
                if not implicit:
                    logging.warning('The variable {} is not explicitly declared. It is implicitly declared as a '
                                    'variable of type float'.format(id))

        self.spec.out_var = id_head;
        self.spec.out_var_field = id_tail;
        self.spec.free_vars.discard(id_head)
        return out

    def visitSpecification_file(self, ctx):
        return self.visit(ctx.specification())

    def visitSpecification(self, ctx):
        out = self.visitChildren(ctx)
        try:
            del self.var_subspec_dict[self.spec.out_var + self.spec.out_var_field]
        except KeyError:
            #raise RTAMTException('Could not remove an entry from var_subspec_dict.')
            pass
        return out

    def visitSpecificationId(self, ctx):
        self.visitChildren(ctx)
        # The specification name is updated only if it is given
        # by the user
        if not ctx.Identifier() is None:
            self.spec.name = ctx.Identifier().getText()

    def str_to_op_type(self, input):
        if input == "<":
            return self.comp_op_mod.StlComparisonOperator.LESS
        elif input == '<=':
            return self.comp_op_mod.StlComparisonOperator.LEQ
        elif input == ">=":
            return self.comp_op_mod.StlComparisonOperator.GEQ
        elif input == ">":
            return self.comp_op_mod.StlComparisonOperator.GREATER
        elif input == "==":
            return self.comp_op_mod.StlComparisonOperator.EQUAL
        else:
            return self.comp_op_mod.StlComparisonOperator.NEQ
