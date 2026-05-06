from compiler import MiniCompiler  # Mengimpor class dari file py utama

source_code = "a ^ 2 + b * c"
symbol_table = {'a': 5, 'b': 10, 'c': 2}

try:
    print(f"Input: {source_code}")
    compiler = MiniCompiler(source_code, symbol_table)
    ast_root = compiler.expr()
    
    print("\n--- Output Three Address Code (TAC) ---")
    compiler.generate_tac(ast_root)
except Exception as e:
    print(f"Error: {e}")