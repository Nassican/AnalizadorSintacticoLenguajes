from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional
from lpp.token import Token

# Aqui se generan 3 nods independientes

# abc -> abstract syntax class

# 1 Nodo abstracto que extiende la clase ABC para representar clases abstractas
# Estos son los nodos principales que extienden todos los demas nodos (ASTNodo, Statement, Expression)


class ASTNode(ABC):

    @abstractmethod
    def token_literal(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

# 2 Es un nodo de un AST
# Nunca vamos a inicializar Statement de forma directa, la vamos a inicializar de forma extensiva

class Statement(ASTNode):
    def __init__(self, token: Token) -> None:
        self.token = token

    def token_literal(self) -> str:
        # Retorna la literal que existe en el token, el pedazo de string de nuestro programa
        return self.token.literal

# 3 Es un nodo de un AST

class Expression(ASTNode):
    def __init__(self, token: Token) -> None:
        self.token = token

    def token_literal(self) -> str:
        return self.token.literal

# Esta es la definicion del programa

class Program(ASTNode):

    def __init__(self, statements: list[Statement]) -> None:
        self.statements = statements

    def token_literal(self) -> str:
        # Verificamos si hay mas de 1 statement
        if len(self.statements) > 0:
            # Regresamos el token literal del PRIMER statement
            # Solo es para el debug, para los tests
            return self.statements[0].token_literal()
        return ''

    # Concatenamos todos los statements
    def __str__(self) -> str:
        out: list[str] = []
        for statement in self.statements:
            out.append(str(statement))

        # ''.join(out) -> Toda la concatenacion hecha
        return ''.join(out)

# Nodo de identificador y letstatement
# LEctura de arriba hacia abajo (de Python)



class Identifier(Expression):
    def __init__(self,
                 token: Token,
                 value: str) -> None:
        super().__init__(token)
        self.value = value

    def __str__(self) -> str:
        return self.value

class LetStatement(Statement):
    def __init__(self, 
                 token: Token, 
                 name: Optional[Identifier] = None, 
                 value: Optional[Expression] = None) -> None:
        # Estamos extendiendo Statement
        super().__init__(token)
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f'{self.token_literal()} {str(self.name)} = {str(self.value)};\n'
    
class LetExpression(Statement):
    def __init__(self,
                 token: Token,
                 arguments: Optional[list[Expression]] = None) -> None:
        super().__init__(token)
        self.arguments = arguments

    def __str__(self) -> str:
        assert self.arguments is not None
        # Transformamos cada argumento a str y se vuelve una lista de str
        arg_list: list[str] = [str(argument) for argument in self.arguments]
        args: str = ', '.join(arg_list)
        return f'{str(self.token.literal)} {args};\n'
    
class Read(Expression):
    def __init__(self,
                 token: Token,
                 arguments: Optional[list[Identifier]] = None) -> None:
        super().__init__(token)
        self.arguments = arguments

    def __str__(self) -> str:
        assert self.arguments is not None
        # Transformamos cada argumento a str y se vuelve una lista de str
        arg_list: list[str] = [str(argument) for argument in self.arguments]
        args: str = ', '.join(arg_list)
        return f'{str(self.token.literal)} {args};\n'
    
class Write(Expression):
    def __init__(self,
                 token: Token,
                 arguments: Optional[list[Expression]] = None) -> None:
        super().__init__(token)
        self.arguments = arguments

    def __str__(self) -> str:
        assert self.arguments is not None
        # Transformamos cada argumento a str y se vuelve una lista de str
        arg_list: list[str] = [str(argument) for argument in self.arguments]
        args: str = ', '.join(arg_list)
        return f'{str(self.token.literal)} {args};\n'    

class ReturnStatement(Statement):

    def __init__(self,
                 token: Token,
                 return_value: Optional[Expression] = None) -> None:
        super().__init__(token)
        self.return_value = return_value

    def __str__(self) -> str:
        return f'{self.token_literal()} {str(self.return_value)};'

class ExpressionStatement(Statement):
    def __init__(self,
                 token: Token,
                 expression: Optional[Expression] = None) -> None:
        super().__init__(token)
        self.expression = expression

    def __str__(self) -> str:
        return str(self.expression)

class Integer(Expression):
    def __init__(self,
                 token: Token,
                 value: Optional[int] = None) -> None:
        super().__init__(token)
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    
class StringLiteral(Expression):

    def __init__(self,
                 token: Token,
                 value: Optional[str] = None) -> None:
        super().__init__(token)
        self.value = value

    def __str__(self) -> str:
        return super().__str__()
    
class Prefix(Expression):
    def __init__(self,
                 token: Token,
                 operator: Optional[str],
                 right: Optional[Expression] = None) -> None:
        super().__init__(token)
        self.operator = operator
        self.right = right

    def __str__(self) -> str:
        return f'({self.operator}{str(self.right)})'
    
class Infix(Expression):
    def __init__(self,
                 token: Token,
                 left: Expression,
                 operator: str,
                 right: Optional[Expression] = None) -> None:
        super().__init__(token)
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self) -> str:
        return f'({str(self.left)} {self.operator} {str(self.right)})'
    
class Boolean(Expression):
    def __init__(self,
                 token: Token,
                 value: Optional[bool] = None) -> None:
        super().__init__(token)
        self.value = value

    def __str__(self) -> str:
        return self.token_literal()
    
class Block(Statement):

    def __init__(self,
                 token: Token,
                 statements: list[Statement]) -> None:
        super().__init__(token)
        self.statements = statements

    def __str__(self) -> str:
        # Nos genera una lista de statements conertidos a strings
        out: list[str] = [str(statement) for statement in self.statements]
   
        
        # Concatenamos todo
        return ''.join(out)
    
class If(Expression):
    def __init__(self,
                 token: Token,
                 condition: Optional[Expression] = None,
                 consequence: Optional[Block] = None,
                 alternative: Optional[Block] = None) -> None:
        super().__init__(token)
        self.condition = condition 
        self.consequence = consequence
        self.alternative = alternative
              

    def __str__(self) -> str:
        out: str = f'\nSi {str(self.condition)}\nEntonces\n{str(self.consequence)}\n'
        # Si hay una alternativa lo concatenamos
        if self.alternative:
            out += f'\nSino\n{str(self.alternative)}\nFinSi\n'
        else:
            out += f'\nFinSi\n'

        return ''.join(out)
    
class While(Expression):
    def __init__(self,
                 token: Token,
                 condition: Optional[Expression] = None,
                 actions: Optional[Block] = None) -> None:
        super().__init__(token)
        self.condition = condition 
        self.actions = actions
              
    
    def __str__(self) -> str:
        without_skip = str(self.condition).replace("\n", '')
        out: str = f'\nMientras {without_skip} hacer\n{str(self.actions)}\n\nFinMientras\n'

        return ''.join(out)

class Forto(Expression):
    def __init__(self,
                 token: Token,
                 start: Optional[LetStatement] = None,
                 end: Optional[Expression] = None,
                 body: Optional[Block] = None) -> None:
        super().__init__(token)
        self.start = start 
        self.end = end
        self.body = body
              

    def __str__(self) -> str:
        out: str = f'\nPara {str(self.start)} hasta {str(self.end)}\n{str(self.body)}\nFinPara\n'

        return ''.join(out)
    
class Asperdo(Expression):
    def __init__(self,
                 token: Token,
                 letNumeric: Optional[Identifier] = None,
                 options: Optional[Block] = None,
                 otherMode: Optional[Block] = None) -> None:
        super().__init__(token)
        self.letNumeric = letNumeric 
        self.options = options
        self.otherMode = otherMode

    def __str__(self) -> str:
        out: str = f'\nSegun {str(self.letNumeric)} hacer \n{str(self.options)}\n'
        # Si hay una alternativa lo concatenamos
        if self.otherMode:
            out += f'DeOtroModo: \n{str(self.otherMode)}\nFinSegun\n'
        else:
            out += f'FinSegun\n'

        return ''.join(out)
    
class StartProgram(Expression):
    def __init__(self,
                 token: Token,
                 name: Optional[Identifier] = None,
                 body: Optional[Block] = None) -> None:
        super().__init__(token)
        self.name = name
        self.body = body
              

    def __str__(self) -> str:
        out: str = f'Programa '

        if self.name:
            out += f'{str(self.name)}\n{str(self.body)}\nFinPrograma'
        else:
            out += f'\n{str(self.body)}\nFinPrograma'

        return ''.join(out)
    

    
