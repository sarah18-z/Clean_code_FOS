def get_symbol(name: str) -> str:
symbol = chemical_symbols.get(name)
if symbol:
    return symbol
else : 
    return "not found"