#JUEGO DE PIEDRA, PAPEL O TIJERA
import random

opciones = ("piedra","papel","tijera")
round = 1
user_win = 0
computer_win = 0
name_user = input("Ingresa tu nombre de usuario para empezar a jugar: ")
while True:
    print("*" * 10)
    print("ROUND",round)
    print("*" * 10) 
    print("USER WIN 🧑",user_win)
    print("COMPUTER WIN 🖥️ ", computer_win)
    user_option = input("piedra, papel o tijera: ")
    user_option = user_option.lower() #convierte todas las entradas del usuario en minuscula

    computer_option = random.choice(opciones)
    print("User option =>", user_option)
    print("Computer option =>",computer_option)
    round += 1
    if not user_option in opciones:
        print("Esa opcion no es valida")
        continue
    if user_option == computer_option:
        print("Empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra le gana a tijera")
            print("Has ganado!")
            user_win += 1
        else:
            print("papel le gana a piedra")
            print("Computer gano!")
            computer_win += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel le gana a piedra")
            print("Has ganado!")
            user_win += 1
        else:
            print("Tijera gana a papel")
            print("Computer gano!")
            computer_win += 1

    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("Has ganado!")
            user_win += 1
        else:
            print("Piedra gana a tijera")
            print("Computer gano!")
            computer_win += 1

    if computer_win == 2:
        print("El computador 🖥️  gano la partida!!")
        break
    elif user_win == 2:
        print(f"{name_user} a ganado la partida!!")
        break
    
        
