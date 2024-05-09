from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
import streamlit as st
import graphviz
from hinnerLexer import hinnerLexer
from hinnerParser import hinnerParser
from hinnerVisitor import hinnerVisitor

class Buit :
    pass
@dataclass
class Node:
    simbol : str
    childs : list[Node]

def NodeType_to_string(a):
    result = ""
    first = True
    if (a.simbol == "->"): 
        result += "("
        for e in a.childs:
            if first: first = False
            else: result += "->"
            result += NodeType_to_string(e)

        result += ")"
    else: result += a.simbol

    return result



class TreeVisitor(hinnerVisitor):
    types = {}
    def visitRoot(self, ctx):
        [a,b] = list(ctx.getChildren())
        return self.visit(a)

    def visitTypeDefStmt(self, ctx):
        [expr, d, Type] = list(ctx.getChildren())
        expr = self.visit(expr)
        Type = self.visit(Type)
        TreeVisitor.types[expr.simbol] = Type
        print(Type)
        print(NodeType_to_string(Type))

    def visitSingleType(self, ctx):
        [T] = list(ctx.getChildren())
        return Node(T.getText(), [])
    
    def visitTypeAssocRight(self, ctx):
        [T1, A, T2] = list(ctx.getChildren())
        T1 = self.visit(T1)
        T2 = self.visit(T2)
        return Node("->", [T1,T2])

    def visitParType(self, ctx):
        [L, Type, R] = list(ctx.getChildren())
        return self.visit(Type)

    def visitExprStmt(self, ctx):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    

    def visitIdent(self, ctx):
        [ident] = list(ctx.getChildren())
        return Node(str(ident), [])
    
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return Node(str(numero), [])
    
    def visitAbstraccioExpr(self, ctx):
        [abstraccio] = list(ctx.getChildren())
        return self.visit(abstraccio)
    
    def visitOperadorINFIX(self, ctx):
        [O] = list(ctx.getChildren())
        return Node(O.getText(), [])
    
    def visitFuncio(self,ctx):
        [_,i,_,e] = list(ctx.getChildren())
        expr = self.visit(e)
        return Node("λ", [Node(str(i), []), expr])
    
    def visitAplicacioExpr(self, ctx):
        [e1,e2] = list(ctx.getChildren())
        e1 = self.visit(e1)
        e2 = self.visit(e2)
        return Node("@", [e1, e2])
    def visitParenthesis(self, ctx):
        [L,e,R] = list(ctx.getChildren())
        return self.visit(e)

def createGraph(root):
    graph = graphviz.Graph()

    queue = []
    i = 0
    queue.append(["n"+str(i), root])
    graph.node("n"+str(i), root.simbol)
    i += 1
    while len(queue) != 0:
        current_node = queue.pop(0)
        for e in current_node[1].childs:
            queue.append(["n"+str(i), e])
            graph.node("n"+str(i), e.simbol)
            graph.edge(current_node[0], "n"+str(i))
            i += 1
        

    return graph


if __name__ == "__main__":
    text = st.text_input(label="Expressió:")
    button_fer = st.button(label="fer")
    if button_fer:
        input_stream = InputStream(text)
        lexer = hinnerLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = hinnerParser(token_stream)
        tree = parser.root()
        if parser.getNumberOfSyntaxErrors() == 0:
            visitor = TreeVisitor()
            graph = visitor.visit(tree)
            if graph != None:
                graph = createGraph(graph)
                st.graphviz_chart(graph)
            st.success(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')
            st.write(tree.toStringTree(recog=parser))
        else:
            st.error(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')
    