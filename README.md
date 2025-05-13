# 📊 relation.py

Relation is a minimal Python library for working with relational data using core
relational algebra concepts such as relations, projections, and (coming soon)
selections, joins, and more.

This library is great for educational use, prototyping query systems, or
experimenting with logic programming ideas.

---

## ✨ Features

- Define named relations with typed schema (keys).
- Populate relations with rows of data.
- Project specific keys (columns).
- Fluent method chaining (like `.populate().projection()`).
- Friendly error messages and schema validation.

---

## 📦 Installation

(support for pip install coming soon).

---

## 📚 Examples

```python
from relation import Relation

# Create a relation with schema (name, age)
users = (
    Relation("users", ("name", "age"))
    .populate([
        ("Carlos", 15),
        ("Lucas", 18),
        ("Maria", 22),
    ])
)

# Project only the 'name' column
user_names = users.projection(("name",))

print(user_names.rows)
# Output: [('Carlos',), ('Lucas',), ('Maria',)]
```
