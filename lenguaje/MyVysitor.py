from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVistor(GrammarVisitor):
    def __init__(self):
        self.memory = {}

#!Defini la accion de asignacion
def visitAssign(self,ctx):
    name=ctx.ID().getText()
    value=self.visit(ctx.expr())#? omtenemos la exprecion 
    self.memory[name]=value# ?lo añade en memoria
#!Defini la asignacion
def visitPrint(self,ctx):
    value=self.visit(ctx.expr())
    print(value) #? imprecion de la Exprecion