import random
player = 0
ai = 0 
print("*** Välkommen till sten sax påse ***")

while player != 4:

    print("1. Sten")
    print("2. Sax")
    print("3. Påse")
    print("4. Avsluta")

    try:
        player = int(input("Gör ett val: "))
    except:
        print("\nDu måste ange en siffra!\n") 

    ai = random.randint(1,3)

    if player == 1 and ai == 1:
        print("du valde ", player)
        print("ai valde ", ai)
        print("DRAW")
    elif player == 1 and ai == 2:
        print("du valde ", player)
        print("ai valde ", ai)
        print("WIN")
    elif player == 1 and ai == 3:
        print("du valde ", player)
        print("ai valde ", ai)
        print("LOSE")
    elif player == 2 and ai == 1:
        print("du valde ", player)
        print("ai valde ", ai)
        print("LOSE")
    elif player == 2 and ai == 2:
        print("du valde ", player)
        print("ai valde ", ai)
        print("DRAW")
    elif player == 2 and ai == 3:
        print("du valde ", player)
        print("ai valde ", ai)
        print("WIN")
    elif player == 3 and ai == 1:
        print("du valde ", player)
        print("ai valde ", ai)
        print("WIN")
    elif player == 3 and ai == 2:
        print("du valde ", player)
        print("ai valde ", ai)
        print("LOSE")
    elif player == 3 and ai == 3:
        print("du valde ", player)
        print("ai valde ", ai)
        print("DRAW")
    elif player == 4:
        print("Välkommen tillbaka!")
    else:
        print("Du gjorde inte ett korrekt val, prova igen")
