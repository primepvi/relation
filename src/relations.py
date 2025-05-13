class Relation:
    def __init__(self, name: str, keys: tuple[str]):
        self.name = name
        self.keys = keys
        self.rows = []

    def _isvalid_row(self, row: tuple[any]):
        if len(self.keys) == 1:
            return True
        return isinstance(row, tuple) and len(row) == len(self.keys)

    def _isvalid_key(self, key: str):
        return key in self.keys

    def populate(self, rows: list[tuple[any]]):
        for row in rows:
            if not self._isvalid_row(row):
                raise TypeError(
                    f"[{self.name}.populate] Invalid row: {row}. Expected a tuple with {len(self.keys)} elements matching keys {self.keys}."
                )
        self.rows = rows
        return self

    def projection(self, keys: tuple[str]):
        for key in keys:
            if not self._isvalid_key(key):
                raise KeyError(
                    f"[{self.name}.projection] Invalid key: '{key}' does not exist in schema {self.keys}."
                )

        rows = [
            tuple(row[i] for i, key in enumerate(self.keys) if key in keys)
            for row in self.rows
        ]
        
        relation = Relation(self.name, keys)
        relation.populate(rows)
        return relation
