import re

class MiniCompiler:
    def __init__(self, source, env):
        # TUGAS 1: Menambahkan '^' ke dalam regex
        self._tokens = iter(re.findall(r'[a-zA-Z_]\w*|\d+(?:\.\d+)?|[+*/()\-\^]', source) + ['?'])
        self._current = None
        self._env = env 
        self._temp_count = 0
        self.advance()

    def advance(self):
        try:
            self._current = next(self._tokens)
        except StopIteration:
            self._current = None

    def expect(self, expected):
        if self._current != expected and not (expected == "ID" and self._current.isalnum()):
            raise ParserError(f"Expected {expected}, found {self._current}")
        token = self._current
        self.advance()
        return token

    def factor(self):
        token = self._current
        if token is not None and token.replace('.', '', 1).isdigit():
            self.advance()
            return Num(float(token) if '.' in token else int(token))
        elif token and token.isalpha():
            if token not in self._env:
                raise ParserError(f"Semantic Error: Undefined variable '{token}'")
            self.advance()
            return Var(token)
        elif token == '(':
            self.advance()
            node = self.expr()
            self.expect(')')
            return node
        raise ParserError(f"Unexpected token: {token}")

    # TUGAS 2: Implementasikan fungsi power()
    # Gunakan pola yang sama dengan term(), namun untuk operator '^'
    def power(self):
        node = self.factor()
        # Tulis logika perulangan while untuk '^' di sini
        return node

    def term(self):
        # TUGAS 3: Hubungkan hierarki ke self.power()
        node = self.factor() # Ubah ini
        while self._current in ('*', '/'):
            op = self._current
            self.advance()
            node = BinOp(left=node, op=op, right=self.factor()) # Dan sesuaikan pemanggilan kanannya
        return node

    def expr(self):
        node = self.term()
        while self._current in ('+', '-'):
            op = self._current
            self.advance()
            node = BinOp(left=node, op=op, right=self.term())
        return node

    def generate_tac(self, node):
        if isinstance(node, Num): return str(node.value)
        if isinstance(node, Var): return node.name
        
        left_val = self.generate_tac(node.left)
        right_val = self.generate_tac(node.right)
        
        self._temp_count += 1
        temp_name = f"t{self._temp_count}"
        print(f"{temp_name} = {left_val} {node.op} {right_val}")
        return temp_name