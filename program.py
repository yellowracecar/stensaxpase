import random
player = 0
ai = 0 
player1 = 0
player2 = 0
meny = 0
p1wins = 0
p2wins = 0
print("*** Välkommen till sten sax påse ***")
while meny != 3:
    print("\n<<< Huvudmeny >>>")
    print("1. player vs player")
    print("2. ai vs player")
    print("3. Quit")
    try:
        meny = int(input("\nVälj spel: "))
    except:
        print("\nDu måste ange en siffra!\n")
    if meny == 1:
        while p1wins or p2wins != 3:
            print("\nplayer 1")
            print("1. Sten")
            print("2. Sax")
            print("3. Påse")
            print("4. Gå tillbaka till huvudmenyn")

            try:
                player1 = int(input("\nGör ett val: "))
            except:
                print("\nDu måste ange en siffra!\n")
            import os
            os.system('cls')

            print("\nplayer 2")
            print("1. Sten")
            print("2. Sax")
            print("3. Påse")

            try:
                player2 = int(input("\nGör ett val: "))
            except:
                print("\nDu måste ange en siffra!\n")

            if player1 == player2:
                print("player1 valde ", player1)
                print("player2 valde ", player2)
                print("DRAW")
            elif player1 == 1 and player2 == 2 :
                print("player1 valde ", player1)
                print("player2 valde ", player2)
                print(" PLAYER 1 WINS")
                p1wins = p1wins + 1
                print(p1wins)
            elif player1 == 1 and player2 == 3:
                print("player1 valde ", player1)
                print("player2 valde ", player2)
                print("PLAYER 2 WINS")
                p2wins = p2wins + 1
                print(p2wins)
            elif player1 == 2 and player2 == 1:
                print("player1 valde ", player1)
                print("player2 valde ", player2)
                print("PLAYER 2 WINS")
                p2wins = p2wins + 1
                print(p2wins)
            elif player1 == 2 and player2 == 3:
                print("player1 valde ", player1)
                print("player2 valde ", player2)
                print("PLAYER 1 WINS")
                p1wins = p1wins + 1
                print(p1wins)
            elif player1 == 3 and player2 == 1:
                print("player1 valde ", player1)
                print("player2 valde ", player2)
                print("PLAYER 1 WINS")
                p1wins = p1wins + 1
                print(p1wins)
            elif player1 == 3 and player2 == 2:
                print("player1 valde ", player1)
                print("player2 valde ", player2)
                print("PLAYER 2 WINS")
                p2wins = p2wins + 1
                print(p2wins)
        else:
            print("")
    elif meny == 2:    
        while player != 4:

            print("\n1. Sten")
            print("2. Sax")
            print("3. Påse")
            print("4. Gå tillbaka till huvudmenyn")

            try:
                player = int(input("\nGör ett val: "))
            except:
                print("\nDu måste ange en siffra!\n") 

            ai = random.randint(1,3)
            if player == ai:
                print("du valde ", player)
                print("du valde ", ai)
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
            elif player == 4:
                print("")
            else:
                print("Du gjorde inte ett korrekt val, prova igen")
else:
    print("Välkommen åter")