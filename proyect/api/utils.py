from antlr4 import*
from lenguaje.GrammarLexer import GrammarLexer
from lenguaje.GrammarParser import GrammarParser
import io
import sys
import lenguaje.MyVysitor as MyVisitor

def run_code(code:str):
    input_stream = InputStream(code)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser= GrammarParser(stream)
    tree= parser.program()
    #! Capturan la salida 
    old_stdout=sys.stdout()
    buf=io.StringIO()
    sys.stdout=buf 
    #!creamos el objeto de nuestro visitor
    visitor = MyVisitor
    #!Visitamos el arbol de nuestro visitor
    visitor.visit(tree)
    #!captura de salidas
    output=buf.getvalue()

    return output