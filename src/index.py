from src.relations import Relation

users = Relation("users", ["name", "age"])
users.populate([("Carlos", 15), ("Lucas", 18), ("Maria", 22)])

print(users.rows)
print(users.projection(("name",)).rows)
print(users.projection(("age",)).rows)
