from Exercici3Visitor import Exercici3Visitor

class TreeVisitor(Exercici3Visitor):
    def __init__(self):
        self.nivell = 0
    def visitSumaORresta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + str(operador))
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1

    def visitMultORdiv(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + str(operador))
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
    
    def visitPot(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + str(operador))
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        print("  " * self.nivell + numero.getText())