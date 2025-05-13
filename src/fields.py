class Key:
    def __init__(self, name: str, type: type):
        self.name = name
        self.type = type
    def isvalid(self, value: any):
        return isinstance(value, self.type)
   
class Column:
    def __init__(self, keymap: dict, relname: str, key: str, value: any):
        relation_key: Key = keymap[key]

        if not relation_key:
            raise KeyError(f"[{relname}.col] Key {key} is not defined in {relname}.")
        if not relation_key.isvalid(value):
            raise TypeError(f"[{relname}.{relation_key.name}.col]: Key '{relation_key.name}' expects type '{relation_key.type.__name__}' but received '{type(value).__name__}'.")
    
        self.key = relation_key
        self.value = value

    def __repr__(self):
        return f"{self.key.name}={self.value}"

class Row:
    def __init__(self, cols: list[Column]):
        self.cols = cols
    def pick(self, keynames: list[str]):
        cols = [col for col in self.cols if col.key.name in keynames]
        return Row(cols)
    def __repr__(self):
        col_reprs = [repr(col) for col in self.cols]
        return f"Row({', '.join(col_reprs)})"
