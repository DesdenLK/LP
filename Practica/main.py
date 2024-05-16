from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
import streamlit as st
import graphviz
import pandas as pd
import pickle
from hinnerLexer import hinnerLexer
from hinnerParser import hinnerParser
from hinnerVisitor import hinnerVisitor

class Buit :
    pass

@dataclass
class Node:
    simbol : str
    tipus  : Arbre
    childs : list[Node]

Arbre = Node | Buit

def NodeType_to_string(a):
    result = ""
    first = True
    if (a.simbol == "->"): 
        result += "("
        for e in a.childs:
            if first: first = False
            else: result += " -> "
            result += NodeType_to_string(e)

        result += ")"
    else: result += a.simbol

    return result



class TreeVisitor(hinnerVisitor):
    def __init__(self, t):
        self.types = t
        self.type = 0

    def increase(self):
        self.type += 1
        return self.type - 1
    
    def isInDict(self, name):
        t = self.type
        for d in self.types:
            if name in d:
                t = d[name]
        if t == self.type: 
            t = Node(f"t{t}", Buit, [])
            self.types[-1][name] = t
            self.increase()
        return t

    def visitRoot(self, ctx):
        [a,b] = list(ctx.getChildren())
        return self.visit(a)

    def visitTypeDefStmt(self, ctx):
        [expr, d, Type] = list(ctx.getChildren())
        expr = self.visit(expr)
        Type = self.visit(Type)
        self.types[0][expr.simbol] = Type


    def visitSingleType(self, ctx):
        [T] = list(ctx.getChildren())
        return Node(T.getText(), Buit,[])
    
    def visitTypeAssocRight(self, ctx):
        [T1, A, T2] = list(ctx.getChildren())
        T1 = self.visit(T1)
        T2 = self.visit(T2)
        return Node("->", Buit, [T1,T2])

    def visitParType(self, ctx):
        [L, Type, R] = list(ctx.getChildren())
        return self.visit(Type)

    def visitExprStmt(self, ctx):
        [expr] = list(ctx.getChildren())
        return self.visit(expr)
    
    def visitIdent(self, ctx):
        [ident] = list(ctx.getChildren())
        ty = self.isInDict(str(ident))
        return Node(str(ident), ty, [])
    
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        ty = self.isInDict(str(numero))
        return Node(str(numero), ty, [])
    
    def visitAbstraccioExpr(self, ctx):
        [abstraccio] = list(ctx.getChildren())
        return self.visit(abstraccio)
    
    def visitOperadorINFIX(self, ctx):
        [O] = list(ctx.getChildren())
        ty = self.isInDict(O.getText())
        return Node(O.getText(), ty, [])
    
    def visitFuncio(self,ctx):
        [_,i,_,e] = list(ctx.getChildren())
        tipus = Node(f"t{self.increase()}", Buit, [])
        self.types.append({})
        id_type = self.isInDict(str(i))
        expr = self.visit(e)
        return Node("λ", tipus, [Node(str(i), id_type, []), expr])
    
    def visitAplicacioExpr(self, ctx):
        [e1,e2] = list(ctx.getChildren())
        tipus = Node(f"t{self.increase()}", Buit, [])
        e1 = self.visit(e1)
        e2 = self.visit(e2)
        return Node("@", tipus, [e1, e2])
    def visitParenthesis(self, ctx):
        [L,e,R] = list(ctx.getChildren())
        return self.visit(e)

def createGraph(root):
    graph = graphviz.Graph()

    queue = []
    i = 0
    t = NodeType_to_string(root.tipus)
    queue.append(["n"+str(i), root])
    graph.node("n"+str(i), f"{root.simbol}\n{t}")
    i += 1
    while len(queue) != 0:
        current_node = queue.pop(0)
        for e in current_node[1].childs:
            queue.append(["n"+str(i), e])
            t = NodeType_to_string(e.tipus)
            graph.node("n"+str(i), f"{e.simbol}\n{t}")
            graph.edge(current_node[0], "n"+str(i))
            i += 1
        

    return graph

def convertDict(types):
    claus = list(types.keys())
    values = types.values()
    v = []
    for val in values:
        v.append(NodeType_to_string(val))
    t = pd.DataFrame(data=v, index=claus, columns=["TYPE"])
    return t


if __name__ == "__main__":
    types = [{}]
    if 'table' in st.session_state:
        types = pickle.loads(st.session_state['table'])
    table = st.table()
    data = convertDict(types[0])
    table.dataframe(data, use_container_width=True)

    text = st.text_input(label="Expressió:")
    button_fer = st.button(label="fer")
    if button_fer:
        input_stream = InputStream(text)
        lexer = hinnerLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = hinnerParser(token_stream)
        tree = parser.root()
        if parser.getNumberOfSyntaxErrors() == 0:
            visitor = TreeVisitor(types)
            graph = visitor.visit(tree)
            if graph != None:
                graph = createGraph(graph)
                st.graphviz_chart(graph)
            else:
                st.session_state['table'] = pickle.dumps(visitor.types)
                data = convertDict(visitor.types[0])
                table.dataframe(data, use_container_width=True)
            st.success(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')
            st.write(tree.toStringTree(recog=parser))
        else:
            st.error(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')
        
    