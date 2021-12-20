class Person:
    name = ""
    money = 0

bob = Person()
bob.name = "Bob"
bob.money = 100

nancy = bob
nancy.name = "nancy"

print(bob.name)
print(nancy.name)

bob.name = "song"
print(nancy.name)