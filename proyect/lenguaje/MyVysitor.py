from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVistor(GrammarVisitor):
    def __init__(self):
        self.memory = {}

#!Definimos la asignacion de asignacion
def visitAssign(self,ctx):
    #? Se optiene el id o en nombre de la variable 
    name=ctx.ID().getText()
    value=self.visit(ctx.expr()) #? omtenemos el valor numerioco o la exprecion 
    self.memory[name]=value # ?lo Almacena en memoria, apartir del nombre y del valor

#!Definimos la Impresion
def visitPrint(self,ctx):
    #? Definimos la exprecion que se desea mostrar
    value=self.visit(ctx.expr())
    print(value) #? imprime el valor 

#! Definimos las expreciones 
def visitExpr(self,ctx): #? busca si existen Id's
    if ctx.ID():
        #? Obtiene en el contexto 
        name= ctx.ID().gestTest()  
        if name not in self.memory:  #? en caso de que no se encuentre, regresa el error
            raise NameError(f"Variable '{name}' no definida")
        return self.memory[name]  #? si la encuentra retorna la variable
    elif ctx.op: #? Busca el operador 
        left=self.visit(ctx.expr(0))#? Vista y obtiene el lado izquierdo 
        right=self.visit(ctx.expr(0))#? Visita y obtiene el lado derecho 
        #? Evalua la operacion a realizar 
        if ctx.op.text == "+":
            return left + right
        if ctx.op.text == "-":
            return left - right
        if ctx.op.text == "*":
            return left * right
        if ctx.op.text == "/":
            # ? Verifica la divicion entre Cero
            if right==0:
                raise ValueError ("Divicianton por cero")
            return left / right
        
        
        