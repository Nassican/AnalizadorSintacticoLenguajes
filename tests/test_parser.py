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
    If
)
from lpp.lexer import Lexer
from lpp.parser import Parser
from typing import cast

# Para hacer los tests

# Generamos nuestro programa como un nodo del ast


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
        Si ( x < y )
            Entonces {
                x;
            }
        FinSi
        '''
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
        self._test_infix_expression(if_expression.condition, 'x', '<', 'y')

        # Comprobamos la consecuencia
        assert if_expression.consequence is not None
        self.assertIsInstance(if_expression.consequence, Block)
        self.assertEquals(len(if_expression.consequence.statements), 1)

        consequence_statement = cast(ExpressionStatement, 
                                     if_expression.consequence.statements[0])
        
        assert consequence_statement.expression is not None
        self._test_identifier(consequence_statement.expression, 'x')

        # Comprobamos la alternativa
        # Nos aseguramos que sea None, que no existe alternativa (Sino)
        self.assertIsNone(if_expression.alternative)

        



    def test_if_else_expression(self) -> None:
        source: str = '''
        Si (x != y) 
            Entonces {
                x;
            } Sino {
                y;
            }
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
        self._test_infix_expression(if_expression.condition, 'x', '!=', 'y')

        # Test consequence
        assert if_expression.consequence is not None
        self.assertIsInstance(if_expression.consequence, Block)
        self.assertEquals(len(if_expression.consequence.statements), 1)

        consequence_statement = cast(ExpressionStatement, if_expression.consequence.statements[0])
        assert consequence_statement.expression is not None
        self._test_identifier(consequence_statement.expression, 'x')

        # Test alternative
        assert if_expression.alternative is not None
        self.assertIsInstance(if_expression.alternative, Block)
        self.assertEquals(len(if_expression.alternative.statements), 1)

        alternative_statement = cast(ExpressionStatement, if_expression.alternative.statements[0])
        assert alternative_statement.expression is not None
        self._test_identifier(alternative_statement.expression, 'y')


















