from fields import Column, Key, Row

class Relation:
    def __init__(self, name: str, keys: list[Key]):
        self._name = name
        self._keys = keys
        self._rows = []
        self._keymap = {k.name: k for k in keys}

    def __getattr__(self, attr) -> Key:
        if attr in self._keymap:
            return self._keymap[attr]
        raise AttributeError(f"Relation '{self._name}' has no attribute '{attr}'.")

    def __getitem__(self, key) -> Key | None:
        return self._keymap[key]

    def to_dict(self) -> dict[str, Key]:
        return { k.name: k for k in self._keys }
    
    def col(self, key: str, value: any):
        return Column(self.to_dict(), self._name, key, value)
    
    def row(self, row: dict):
        cols = [self.col(k, v) for k, v in row.items()]
        return Row(cols)

    def populate(self, rows: list[Row]):
        self._rows = rows
        return self

    def project(self, keys: list[Key]):
        schema_dict = self.to_dict()

        for key in keys:
            if not isinstance(key, Key):
                raise TypeError(f"[{self._name}.project] Expected Key instance, got {type(key).__name__}")
            if key.name not in schema_dict:
                raise KeyError(f"[{self._name}.project] Invalid key: '{key.name}' does not exist in this relation.")

        rows = [row.pick([key.name for key in keys]) for row in self._rows]
        projected_keys = [k for k in self._keys if k.name in {key.name for key in keys}]

        return Relation(self._name, projected_keys).populate(rows)
