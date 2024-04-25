from Exercici7Visitor import Exercici7Visitor

class EvalVisitor(Exercici7Visitor):
    lvars = {}

    def visitRoot(self, ctx):
        statements = list(ctx.getChildren())
        for e in statements:
            self.visit(e)

    def visitAssignStmt(self, ctx):
        [name, _, expr] = list(ctx.getChildren())
        e1 = self.visit(expr)
        EvalVisitor.lvars[name.getText()] = e1

    def visitIfStmt(self, ctx):
        children = list(ctx.getChildren())
        expr = children[1]
        statements = children[3:]
        expr = self.visit(expr)
        if (expr is True):
            for e in statements:
                self.visit(e)

    def visitWhileStmt(self, ctx):
        children = list(ctx.getChildren())
        expr = children[1]
        statements = children[3:]
        cond = self.visit(expr)
        while cond is True:
            for e in statements:
                self.visit(e)
            cond = self.visit(expr)

    def visitWriteStmt(self, ctx):
        [write, name] = list(ctx.getChildren())
        e1 = self.visit(name)
        print(e1)
    
    def visitExprStmt(self, ctx):
        [expr] = list(ctx.getChildren())
        e1 = self.visit(expr)
        return e1 
    
    def visitEqual(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        e1 = self.visit(expressio1)
        e2 = self.visit(expressio2)
        return e1 == e2

    def visitDiff(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        e1 = self.visit(expressio1)
        e2 = self.visit(expressio2)
        return e1 != e2 

    def visitIdentExpr(self, ctx):
        [id] = list(ctx.getChildren())
        return EvalVisitor.lvars[str(id)]

    def visitSumaORresta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        e1 = self.visit(expressio1)
        e2 = self.visit(expressio2)
        return (e1 + e2) if str(operador) == '+' else e1 - e2
    
    def visitSumaORresta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        e1 = self.visit(expressio1)
        e2 = self.visit(expressio2)
        return (e1 + e2) if str(operador) == '+' else e1 - e2
    
    def visitMultORdiv(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        e1 = self.visit(expressio1)
        e2 = self.visit(expressio2)
        return (e1 * e2) if str(operador) == '*' else e1 / e2
    
    def visitPot(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        e1 = self.visit(expressio1)
        e2 = self.visit(expressio2)
        return e1**e2
    
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())