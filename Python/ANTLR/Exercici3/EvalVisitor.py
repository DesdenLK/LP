from Exercici3Visitor import Exercici3Visitor

class EvalVisitor(Exercici3Visitor):
    def visitRoot(self, ctx):
        [expressio] = list(ctx.getChildren())
        print(self.visit(expressio))
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