from re import match
from lpp.token import Token, TokenType, lookup_token_type



class Lexer:
    def __init__(self, source:str) -> None:
      self._source: str = source
      self._character: str = ''
      self._read_position: int = 0
      self._position: int = 0

      self._read_character()

    def next_token(self) -> Token:
      self._skip_whitespace()

      if match(r"^=$", self._character):
        if self._peek_character() == '=':
            token = self._make_two_character_token(TokenType.EQUALS)
        else:
            token = Token(TokenType.ASSIGN, self._character)
      elif match(r"^\+$", self._character):
          token = Token(TokenType.PLUS, self._character)
      elif match(r"^\($", self._character):
          token = Token(TokenType.LPAREN, self._character)
      elif match(r"^\)$", self._character):
          token = Token(TokenType.RPAREN, self._character)
      elif match(r"^{$", self._character):
          token = Token(TokenType.LBRACE, self._character)
      elif match(r"^}$", self._character):
          token = Token(TokenType.RBRACE, self._character)
      elif match(r"^,$", self._character):
          token = Token(TokenType.COMMA, self._character)
      elif match(r"^:$", self._character):
          token = Token(TokenType.COLON, self._character)
      elif match(r"^;$", self._character):
          token = Token(TokenType.SEMICOLON, self._character)
      elif match(r"^$", self._character):
          token = Token(TokenType.EOF, self._character)
      elif match(r"^<$", self._character):
          token = Token(TokenType.LT, self._character)
      elif match(r"^>$", self._character):
          token = Token(TokenType.MT, self._character)
      elif match(r"^-$", self._character):
          token = Token(TokenType.MINUS, self._character)
      elif match(r"^\/$", self._character):
          token = Token(TokenType.DIVIDE, self._character)
      elif match(r"^\*$", self._character):
          token = Token(TokenType.MULT, self._character)
      elif match(r"^!$", self._character):
        if self._peek_character() == '=':
            token = self._make_two_character_token(TokenType.NOTEQUALS)
        else:
            token = Token(TokenType.NOT, self._character)
      elif self._is_letter(self._character):
          literal = self._read_identifier()  # 5
          token_type = lookup_token_type(literal) # INT
          return Token(token_type, literal)
      
      elif self._is_number(self._character):
          literal = self._read_number()
          if self._character == ".":
              self._read_character()
              sufix = self._read_number()
              return Token(TokenType.FLOAT, f"{literal}.{sufix}")
          return Token(TokenType.INT, literal)
      elif match(r'^"$', self._character):
            literal = self._read_string()
            return Token(TokenType.STRING, literal)
      else:
        token = Token(TokenType.ILLEGAL, self._character)

      self._read_character()

      return token
    
    def _read_string(self) -> str:
        self._read_character()

        initial_position = self._position

        while self._character != '"' \
                and self._read_position <= len(self._source):
            self._read_character()

        string = self._source[initial_position:self._position]

        self._read_character()

        return string

    def _read_character(self) -> None:
      if self._read_position >= len(self._source):
        self._character = ''
      else:
        self._character = self._source[self._read_position]

      self._position = self._read_position
      self._read_position += 1

    def _is_letter(self, character: str) -> bool:
      # Retorna si es letra/String
      return bool(match(r'^[a-záéíóúA-ZÁÉÍÓÚñÑ_]$', character))
    
    def _is_number(self, character: str) -> bool:
      # Retorna si es numero\int
      return bool(match(r'^\d$', character))  
    
    def _read_identifier(self) -> str:
      initial_position = self._position

      while self._is_letter(self._character) or self._is_number(self._character): #Sigamos encontrando letras
        self._read_character() # avanza 1 caracter

      return self._source[initial_position:self._position]
    
    def _read_number(self) -> str:
      initial_position = self._position
      while self._is_number(self._character):
        self._read_character()

      return self._source[initial_position:self._position]

    def _skip_whitespace(self) -> None:
      while match(r'^\s$', self._character):
        self._read_character()

    # Caracter siguiente
    def _peek_character(self) -> str:
        if self._read_position >= len(self._source):
            return ''
        return self._source[self._read_position]
      
    
    def _make_two_character_token(self, token_type: TokenType) -> Token:
        prefix = self._character
        self._read_character()
        suffix = self._character

        return Token(token_type, f'{prefix}{suffix}')