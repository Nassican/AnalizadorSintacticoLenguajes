from unittest import TestCase
from lpp.ast import (
    LetStatement,
    Program,
    ReturnStatement,
    Expression,
    ExpressionStatement,
    Identifier,
    Integer,
    Prefix,
    Infix,
    Boolean,
    Block,
    If,
    While,
    Forto,
    StartProgram,
    Asperdo,
    StringLiteral,
    LetExpression,
    Write,
)
from lpp.lexer import Lexer
from lpp.parser import Parser
from typing import cast

# Para hacer los tests

# Generamos nuestro programa como un nodo del ast
# Esto es para que el test sepa que es un programa

class ParserTest(TestCase):

    def test_parse_program(self) -> None:
        source: str = 'variable x = 5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        # Verificar que hay "algo" dentro del programa
        self.assertIsNotNone(program)
        # Verificar que el programa es del tipo programa
        self.assertIsInstance(program, Program)

    def test_let_statement(self) -> None:
        source: str = '''
            variable x = 5;
            variable y = 10;
            variable foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertEqual(len(program.statements), 3)

        for statement in program.statements:
            self.assertEqual(statement.token_literal(), 'variable')
            self.assertIsInstance(statement, LetStatement)

    def test_names_in_let_statements(self) -> None:
        source: str = '''
            variable x = 5;
            variable y = 10;
            variable foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        names: list[str] = []
        for statement in program.statements:
            # el cast es para que el test sepa LetStatement sea literalmente un statement
            statement = cast(LetStatement, statement)
            assert statement.name is not None
            names.append(statement.name.value)

        expected_names: list[str] = ['x', 'y', 'foo']

        self.assertEquals(names, expected_names)

    def test_parse_errors(self) -> None:
        source: str = 'variable x 5;'

        lexer: Lexer = Lexer(source)  # No le importa la gramatica
        parser: Parser = Parser(lexer)  # Si le importa la gramatica

        program: Program = parser.parse_program()

        self.assertEquals(len(parser.errors), 1)

    def test_return_statement(self) -> None:
        source: str = '''
            retorna 5;
            retorna foo;
        '''

        lexer: Lexer = Lexer(source)  # No le importa la gramatica
        parser: Parser = Parser(lexer)  # Si le importa la gramatica

        program: Program = parser.parse_program()

        self.assertEquals(len(program.statements), 2)

        for statement in program.statements:
            self.assertEquals(statement.token_literal(), 'retorna')
            self.assertIsInstance(statement, ReturnStatement)

    def test_identifier_expression(self) -> None:
        source: str = 'foobar;'
        lexer: Lexer = Lexer(source)  # No le importa la gramatica
        parser: Parser = Parser(lexer)  # Si le importa la gramatica

        program: Program = parser.parse_program()

        # Funcion Auxiliar que dice los errores
        self._test_program_statements(parser, program)

        expression_statement = cast(ExpressionStatement, program.statements[0])

        assert expression_statement.expression is not None

        self._test_literal_expression(
            expression_statement.expression, 'foobar')

    def _test_program_statements(self,
                                 parser: Parser,
                                 program: Program,
                                 expected_statement_count: int = 1) -> None:
        if parser.errors:
            print(parser.errors)
        self.assertEquals(len(parser.errors), 0)
        self.assertEquals(len(program.statements), expected_statement_count)
        self.assertIsInstance(program.statements[0], ExpressionStatement)

    def _test_literal_expression(self,
                                 expression: Expression,
                                 expected_value: any) -> None:
        value_type: type = type(expected_value)

        if value_type == str:
            self._test_identifier(expression, expected_value)
        elif value_type == int:
            self._test_integer(expression, expected_value)
        elif value_type == bool:
            self._test_boolean(expression, expected_value)
        else:
            self.fail(f'Tipo de expresión no controlada. Obtuvo={value_type}')

    def _test_identifier(self,
                         expression: Expression,
                         expected_value: str) -> None:
        self.assertIsInstance(expression, Identifier)

        identifier = cast(Identifier, expression)
        self.assertEquals(identifier.value, expected_value)
        self.assertEquals(identifier.token.literal, expected_value)

    def _test_string_literal(self,
                         expression: Expression,
                         expected_value: str) -> None:
        self.assertIsInstance(expression, StringLiteral)

        stringliteral = cast(StringLiteral, expression)
        self.assertEquals(stringliteral.value, expected_value)
        self.assertEquals(stringliteral.token.literal, expected_value)
    '''

    5;
    variable x = 5;
    suma(5, 10);
    5 + 5 + 5;

    '''

    def test_integer_expressions(self) -> None:
        source: str = '5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        expression_statement = cast(ExpressionStatement, program.statements[0])

        assert expression_statement.expression is not None
        self._test_literal_expression(expression_statement.expression, 5)

    def _test_integer(self,
                      expression: Expression,
                      expected_value: int) -> None:
        self.assertIsInstance(expression, Integer)

        integer = cast(Integer, expression)
        self.assertEquals(integer.value, expected_value)
        self.assertEquals(integer.token.literal, str(expected_value))

    def _test_boolean(self,
                      expression: Expression,
                      expected_value: Boolean) -> None:
        self.assertIsInstance(expression, Boolean)

        boolean = cast(Boolean, expression)
        self.assertEquals(boolean.value, expected_value)
        self.assertEquals(boolean.token.literal, 'verdadero' if expected_value else 'falso')
        
    '''
    Operadores de prefijo:
    -5;
    !foo;
    5 + -10;

    Test
    Nodo
    Identificar funcion especifica para parsear el nodo y
    registrarla como infix o prefix
    '''

    def test_prefix_expressions(self) -> None:
        source: str = '!5; -15;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser,
                                      program,
                                      expected_statement_count=2)
        
        for statement, (expected_operator, expected_value) in zip(
            program.statements, [('!', 5), ('-', 15)]):
            statement = cast(ExpressionStatement, statement)
            self.assertIsInstance(statement.expression, Prefix)

            prefix = cast(Prefix, statement.expression)
            self.assertEquals(prefix.operator, expected_operator)

            assert prefix.right is not None
            self._test_literal_expression(prefix.right, expected_value)

    '''
    Ejemplos de infix:
    (el signo de en medio es infix)

    5 + 5;
    5 - 5;
    5 * 5;
    5 / 5;
    5 > 5;
    5 < 5;
    5 == 5;
    5 != 5;
    '''
    def test_infix_expressions(self) -> None:
        source: str='''
            5 + 5;
            5 - 5;
            5 * 5;
            5 / 5;
            5 > 5;
            5 < 5;
            5 == 5;
            5 != 5;
        '''
        
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program, expected_statement_count=8)

        expected_operators_and_values: list[tuple[any, str, any]] = [
            (5, '+', 5),
            (5, '-', 5),
            (5, '*', 5),
            (5, '/', 5),
            (5, '>', 5),
            (5, '<', 5),
            (5, '==', 5),
            (5, '!=', 5),
            (5, '=', 5),
            (5, "&", 5,)
        ]

        for statement, (expected_left, expected_operator, expected_right) in zip(
            program.statements, expected_operators_and_values):
            statement = cast(ExpressionStatement, statement)
            assert statement.expression is not None
            self.assertIsInstance(statement.expression, Infix)
            self._test_infix_expression(
                statement.expression,
                expected_left,
                expected_operator,
                expected_right)

    def _test_infix_expression(
            self,
            expression: Expression,
            expected_left: any,
            expected_operator: str,
            expected_right: any):
        infix = cast(Infix, expression)

        assert infix.left is not None
        self._test_literal_expression(infix.left, expected_left)

        assert infix.right is not None
        self._test_literal_expression(infix.right, expected_right)

    '''
    Booleanos

    verdadero;
    falso;
    variable foo = verdadero;
    variable bar = falso;
    '''
    
    def test_boolean_expression(self) -> None:
        source: str='verdadero; falso;'
        
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program, expected_statement_count=2) # True False
        
        expected_values: list[bool] = [True, False]

        for statement, expected_value in zip(program.statements, expected_values):
            expression_statement = cast(ExpressionStatement, statement)

            assert expression_statement is not None
            self._test_literal_expression(expression_statement.expression, expected_value)
    
    '''
        1str: programa inicial, 
        2str: Orden de precedencia dentro del programa
        int: Cuantos statements se espera del programa
    '''

    def test_operator_precedence(self) -> None:
        test_sources: list[tuple[str, str, int]] = [
            ('-a * b;', '((-a) * b)', 1),
            ('!-a;', '(!(-a))', 1),
            ('a + b + c;', '((a + b) + c)', 1),
            ('a + b - c;', '((a + b) - c)', 1),
            ('a * b * c;', '((a * b) * c)', 1),
            ('a + b / c;', '(a + (b / c))', 1),
            ('a * b / c;', '((a * b) / c)', 1),
            ('a + b * c + d / e - f;', '(((a + (b * c)) + (d / e)) - f)', 1),
            ('5 > 4 == 3 < 4;', '((5 > 4) == (3 < 4))', 1),
            ('3 - 4 * 5 == 3 * 1 + 4 * 5;', '((3 - (4 * 5)) == ((3 * 1) + (4 * 5)))', 1),
            ('3 + 4; -5 * 5;', '(3 + 4)((-5) * 5)', 2),
            ('verdadero;', 'verdadero', 1),
            ('falso;', 'falso', 1),
            ('3 > 5 == verdadero;', '((3 > 5) == verdadero)', 1),
            ('3 < 5 == falso;', '((3 < 5) == falso)', 1),
            ('1 + (2 + 3) + 4;', '((1 + (2 + 3)) + 4)', 1),
            ('(5 + 5) * 2;', '((5 + 5) * 2)', 1),
            ('2 / (5 + 5);', '(2 / (5 + 5))', 1),
            ('-(5 + 5);', '(-(5 + 5))', 1),
        ]

        for source, expected_result, expected_statement_count in test_sources:
            lexer: Lexer = Lexer(source)
            parser: Parser = Parser(lexer)

            program: Program = parser.parse_program()

            self._test_program_statements(parser, program, expected_statement_count)
            self.assertEquals(str(program), expected_result)

    def test_if_expression(self) -> None:
        source: str = '''
        Si (a > b) Entonces
            c;
		FinSi
        '''
        # cambiar c; por a=b+c;
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        # Esto es para comprobar que el primer statement sea un ExpressionStatement y con eso
        # sabemos que tenemos un expression que debe ser un if
        if_expression = cast(If, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(if_expression, If)

        # Comprobamos la condicion
        assert if_expression.condition is not None
        self._test_infix_expression(if_expression.condition, 'a', '>', 'b')

        # Comprobamos la consecuencia
        assert if_expression.consequence is not None
        self.assertIsInstance(if_expression.consequence, Block)
        self.assertEquals(len(if_expression.consequence.statements), 1)

        consequence_statement = cast(ExpressionStatement, 
                                     if_expression.consequence.statements[0])
        
        assert consequence_statement.expression is not None
        self._test_identifier(consequence_statement.expression, 'c')

        # Comprobamos la alternativa
        # Nos aseguramos que sea None, que no existe alternativa (Sino)
        self.assertIsNone(if_expression.alternative)
      
    def test_if_else_expression(self) -> None:
        source: str = '''
        Si (x > y) 
            Entonces 
                x;
            Sino 
                y;
        FinSi
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        # Test correct node type
        if_expression = cast(If, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(if_expression, If)

        # Test condition
        assert if_expression.condition is not None
        self._test_infix_expression(if_expression.condition, 'x', '>', 'y')

        # Test Actions
        assert if_expression.consequence is not None
        self.assertIsInstance(if_expression.consequence, Block)
        self.assertEquals(len(if_expression.consequence.statements), 1)

        consequence_statement = cast(ExpressionStatement, if_expression.consequence.statements[0])
        assert consequence_statement.expression is not None
        self._test_identifier(consequence_statement.expression, 'x')

        # Test Alternative
        assert if_expression.alternative is not None
        self.assertIsInstance(if_expression.alternative, Block)
        self.assertEquals(len(if_expression.alternative.statements), 1)

        alternative_statement = cast(ExpressionStatement, if_expression.alternative.statements[0])
        assert alternative_statement.expression is not None
        self._test_identifier(alternative_statement.expression, 'y')


    def test_while_expression(self) -> None:
        source: str = '''
        Mientras (x < y) hacer
            x;
        FinMientras
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        # Test correct node type
        while_expression = cast(While, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(while_expression, While)

        # Test condition
        assert while_expression.condition is not None
        self._test_infix_expression(while_expression.condition, 'x', '<', 'y')

        # Test Actions
        assert while_expression.actions is not None
        self.assertIsInstance(while_expression.actions, Block)
        self.assertEquals(len(while_expression.actions.statements), 1)

        action_statement = cast(ExpressionStatement, while_expression.actions.statements[0])
        assert action_statement.expression is not None
        self._test_identifier(action_statement.expression, 'x')

    def test_for_expression(self) -> None:
        source: str = '''
        Para a = c hasta b
	        a;
        FinPara
        '''

        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        # Test correct node type
        forto_expression = cast(Forto, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(forto_expression, Forto)

        # Test condition
        assert forto_expression.start is not None
        self._test_infix_expression(forto_expression.start, 'a', '=', 'c')

        # Test End
        assert forto_expression.end is not None
        self._test_literal_expression(forto_expression.end, 'b')


        # Test Body
        assert forto_expression.body is not None
        self.assertIsInstance(forto_expression.body, Block)
        self.assertEquals(len(forto_expression.body.statements), 1)

        body_statement = cast(ExpressionStatement, forto_expression.body.statements[0])
        assert body_statement.expression is not None
        self._test_identifier(body_statement.expression, 'a')

    def test_program_without_name(self) -> None:
        source: str = '''
        Programa
            2;
        FinPrograma
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        # Test correct node type
        code = cast(StartProgram, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(code, StartProgram)

        assert code.body is not None
        self.assertIsInstance(code.body, Block)
        self.assertEquals(len(code.body.statements), 1)

        body_statement = cast(ExpressionStatement, code.body.statements[0])
        assert body_statement.expression is not None
        self._test_integer(body_statement.expression, 2)

    def test_program_with_name(self) -> None:
        source: str = '''
        Programa test
            2;
        FinPrograma
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        # Test correct node type
        code = cast(StartProgram, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(code, StartProgram)

        assert code.name is not None
        self._test_literal_expression(code.name, 'test')

        assert code.body is not None
        self.assertIsInstance(code.body, Block)
        self.assertEquals(len(code.body.statements), 1)

        body_statement = cast(ExpressionStatement, code.body.statements[0])
        assert body_statement.expression is not None
        self._test_integer(body_statement.expression, 2)

    def test_asper(self) -> None:
        source: str = '''
        Segun var hacer
            1:
                a;
            2: 
                b;
        FinSegun
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        # Test correct node type
        asperdo = cast(Asperdo, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(asperdo, Asperdo)

        assert asperdo.letNumeric is not None
        self._test_literal_expression(asperdo.letNumeric, 'var')

        assert asperdo.options is not None
        self.assertIsInstance(asperdo.options, Block)
        self.assertEquals(len(asperdo.options.statements), 6)

    def test_asper_othermode(self) -> None:
        source: str = '''
        Segun var hacer
            1:
                a;
            2: 
                b;
            DeOtroModo:
                c;
        FinSegun
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        # Test correct node type
        asperdo = cast(Asperdo, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(asperdo, Asperdo)

        assert asperdo.letNumeric is not None
        self._test_literal_expression(asperdo.letNumeric, 'var')

        assert asperdo.options is not None
        self.assertIsInstance(asperdo.options, Block)
        self.assertEquals(len(asperdo.options.statements), 6)

        assert asperdo.otherMode is not None
        self.assertIsInstance(asperdo.otherMode, Block)
        self.assertEquals(len(asperdo.otherMode.statements), 1)

    def test_let_variables(self) -> None:
        source: str = '''
            Doble x, y, z;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
    
        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        letexpression = cast(LetExpression, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(letexpression, LetExpression)

        assert letexpression.arguments is not None
        self.assertEquals(len(letexpression.arguments), 3)
        self._test_identifier(letexpression.arguments[0], 'x')
        self._test_identifier(letexpression.arguments[1], 'y')
        self._test_identifier(letexpression.arguments[2], 'z')

    def test_let_write_variables(self) -> None:
        source: str = '''
            Escribir "a =", a, "b =", b;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
    
        program: Program = parser.parse_program()

        self._test_program_statements(parser, program)

        write = cast(Write, cast(ExpressionStatement, program.statements[0]).expression)
        self.assertIsInstance(write, LetExpression)

        assert write.arguments is not None
        self.assertEquals(len(write.arguments), 4)
        self.assertEquals(write.arguments[0], 'a =')
        self.assertEquals(write.arguments[1], 'a')
        self.assertEquals(write.arguments[2], 'b =')
        self.assertEquals(write.arguments[3], 'b')

    def test_string_literal_expression(self) -> None:
        source: str = '"hello world!"'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()

        expression_statement = cast(ExpressionStatement, program.statements[0])
        string_literal = cast(StringLiteral, expression_statement.expression)
        self.assertIsInstance(string_literal, StringLiteral)
        self.assertEquals(string_literal.value, 'hello world!')


'Programa uno Mientras (i < 10) hacer Si (a < b) Entonces Si (x < y) Entonces 9*8/6-5/9/78*23; FinSi FinSi FinMientras Para i=0 hasta a c=c+1; Para a=1 hasta b a; FinPara FinPara FinPrograma'



        



