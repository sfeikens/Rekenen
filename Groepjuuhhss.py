import random
Teller=0
Groepje=0
probeer_opnieuw=1
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
    'Daniel',
    'Armin',
    'Jovan',
    'Ward',
    'Stefan',
    'Caelan',
    'Noah',
    'Kaydeon',
    'Sven W.',
    'Phoenix']
while probeer_opnieuw==1:
    try:
         Hoeveel=int(input("hoeveel mensen wil je in een groepje? "))
    except:
         print("geldig getal AUB")
    else:
         probeer_opnieuw=0
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