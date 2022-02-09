from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor

class PrintNameAstVisitor(AbstractAstVisitor):
    def visitUnary(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return node.__class__.__name__ + '(' + op + ')'

    def visitBinary(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' +  op1 + ')' + node.__class__.__name__ + '(' + op2 + ')'

    def visitLeaf(self, node, *args, **kwargs):
        return node.__class__.__name__
