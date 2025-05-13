# 📊 relation.py

Relation is a minimal Python library for working with relational data using core
relational algebra concepts such as relations, projections, and (coming soon)
selections, joins, and more.

This library is great for educational use, prototyping query systems, or
experimenting with logic programming ideas.

---

## ✨ Features

- Define named **relations** with strongly-typed **schemas**
- Compose **rows** using column definitions that validate types
- Perform operations like `.project()` to select specific attributes
- Access schema keys as attributes (e.g. `users.name`)
- Fluent API with method chaining
- Helpful error messages for debugging

---

## 📦 Installation

(support for pip install coming soon).

---

## 📚 Examples

```py
from relations import Relation, Key

# Define a relation with typed schema
users = Relation("users", [
    Key("name", str),
    Key("age", int)
])

# Populate the relation with typed rows
users = users.populate([
    users.row({ "name": "Carlos", "age": 19 }),
    users.row({ "name": "Robersvaldo", "age": 45 }),
])

# Project only the 'age' column
ages = users.project([users.age])

# Output: [Row(age=19), Row(age=18)]
print(ages._rows)
```
