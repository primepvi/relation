from relations import Relation, Key

users = Relation("users", [
    Key("name", str),
    Key("age", int) 
])

users = users.populate([
    users.row({ "name": "Pedro", "age": 19 }),
    users.row({ "name": "Julia", "age": 18 })
]).project([users.name])

print(users._rows)