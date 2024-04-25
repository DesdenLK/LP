from Exercici4Visitor import Exercici4Visitor

class EvalVisitor(Exercici4Visitor):
    lvars = {}

    def visitRoot(self, ctx):
        statements = list(ctx.getChildren())
        for e in statements:
            p = self.visit(e)
            if p != None:
                print(p)

    def visitAssignStmt(self, ctx):
        [name, _, expr] = list(ctx.getChildren())
        e1 = self.visit(expr)
        EvalVisitor.lvars[name.getText()] = e1

    def visitWriteStmt(self, ctx):
        [write, name] = list(ctx.getChildren())
        e1 = self.visit(name)
        return e1
    
    def visitExprStmt(self, ctx):
        [expr] = list(ctx.getChildren())
        e1 = self.visit(expr)
        return e1 

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