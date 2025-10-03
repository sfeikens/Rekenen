#dit zijn de variabelen

score=0
De_beurt=0
tafel=input("welke tafel wil je oefenen?")

#De loop

while(int(De_beurt))<10:
    De_beurt+=1
    print(De_beurt,"*",tafel,"=?")
    if int(input())==(int(De_beurt)*int(tafel)):
        score+=1
        print("correct!")
    else:
        print("fout!")
print("je score is",score)