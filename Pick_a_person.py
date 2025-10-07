import random
counter=0
people = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Judy","Kevin", "Laura", "Mallory", "Niaj", "Olivia"]
hoeveel=input("hoeveel mensen wil je kiezen? ")
while counter != int(hoeveel):
    person = random.choice(people)
    print(person)
    people.remove(person)
    counter += 1