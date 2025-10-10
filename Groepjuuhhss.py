import random
Teller=0
Groepje=0
Mensen = ['Raad',
    'Josip',
    'Roan',
    'Cris',
    'Kourosh',
    'Sven F.',
    'Anas',
    'Jeffry',
    'Atilla',
    'Ammaar',
    'Ilia',
    'Lion',
    'Orhan',
    'DaniÃ«l',
    'Armin',
    'Jovan',
    'Ward',
    'Stefan',
    'Caelan',
    'Noah',
    'Kaydeon',
    'Sven W.',
    'Phoenix']
Hoeveel=input("hoeveel mensen wil je in een groepje? ")
while len(Mensen) > 0:
    Groepje += 1
    Teller=0
    print("Groepje", Groepje)
    while Teller != int(Hoeveel):
        if len(Mensen) == 0:
            break
        else:
            Persoon = random.choice(Mensen)
            print(Persoon)
            Mensen.remove(Persoon)
            Teller += 1