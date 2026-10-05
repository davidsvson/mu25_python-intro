import random

wordlist = ["apelsin", "dator", "cykel", "äpple"]
secret_word = random.choice(wordlist)
print(secret_word)


guessed_word = input("Gissa ordet:")
print(guessed_word)

if guessed_word == secret_word:
    print("Grattis du klarade det")
else:
    print("Fel")


# version 1 slumpa fram ett ord jämför ordet med gissat ord

# version 2 skapa en loop så att man kan gissa flera gånger

# version 3 jämför varje bokstav i orden, skriv ut om någon bokstav är samma plats
    # jämför en bokstav i taget
    
# version 4 - indikera även om rätt bokstav men fel plats



