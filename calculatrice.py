def Calculatrice():
    while True:  
        a = input("Choisir un nombre : ")
        op = input("Choisir une opération (+, -, /, *) : ")
        b = input("Choisir un nombre : ")

        if type(a) != int :
            print("Erreur : A n'est pas un nombre. \n")
            continue
        if type(b) != int :
            print("Erreur : B n'est pas un nombre. \n")
            continue

        if op == "+":
            total = a + b
        elif op == "-":
            total = a - b
        elif op == "*":
            total = a * b
        elif op == "/":
            total = a / b
        else:
            print("Erreur : opération inconnue. \n")
            continue  

        return "Voici le résultat :", total

print(Calculatrice())
