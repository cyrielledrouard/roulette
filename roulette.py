from random import randrange
from math import ceil


def verification_argent_disponible(argent):
    verif_1 = False
    while not verif_1:
        try:
            argent = int(argent)
            assert argent > 0
            verif_1 = True
        except ValueError:
            argent = input("Veuillez entrer un nombre entier.")
        except AssertionError:
            argent = input("Veuillez entrer un nombre strictement positif.")
    return argent


def verification_numero(num):
    verif_2 = False
    while not verif_2:
        try:
            num = int(num)
            assert 0 <= num <= 36
            verif_2 = True
        except ValueError:
            num = input("Veuillez entrer un nombre entier.")
        except AssertionError:
            num = input("Veuillez entrer un nombre compris entre 0 et 36.")
    return num


def verification_mise(mise, argent):
    verif_3 = False
    while not verif_3:
        try:
            mise = int(mise)
            assert 0 < mise <= argent
            verif_3 = True
        except ValueError:
            mise = input("Veuillez entrer un nombre entier.")
        except AssertionError:
            mise = input("Veuillez entrer un nombre positif et inférieur ou égal à votre argent disponible.")
    return mise


def calcul_gain(argent, mise, num_gagnant, num_mise):
    argent_disponible = argent - mise
    if num_gagnant == num_mise:
        mise = 3 * mise
        print("Bravo, vous remportez trois fois votre mise.")
    elif num_gagnant % 2 == num_mise % 2:
        mise = 0.5 * mise
        print("Presque,vous remportez la moitié de votre mise.")
    else:
        mise = 0
        print("Dommage, vous avez perdu votre mise.")
    argent_disponible = ceil(argent_disponible + mise)
    return argent_disponible


print("Bienvenue dans le jeu de la roulette ! Vous devez miser sur un nombre compris entre 0 et 36.")
argent_disponible = input("De combien d'argent disposez-vous ?")
argent_disponible = verification_argent_disponible(argent_disponible)
jouer = "Y"

while argent_disponible > 0 and jouer.upper() == "Y":
    num_mise = input("Sur quel nombre voulez-vous miser ?")
    num_mise = verification_numero(num_mise)
    print("Vous avez misé sur le numéro :", num_mise)

    mise = input("Quelle est votre mise ?")
    mise = verification_mise(mise, argent_disponible)
    print("Vous avez misé", mise, "euros.")

    num_gagnant = randrange(37)
    print("Le numéro gagnant est :", num_gagnant)

    argent_disponible = calcul_gain(argent_disponible, mise, num_gagnant, num_mise)
    print("Vous disposez de", argent_disponible, "euros.")

    if argent_disponible == 0:
        input("Appuyez sur une touche pour quitter.")
        break

    jouer = input(
        "Voulez-vous jouer de nouveau à la roulette ? Si oui, tapez y sinon tapez sur n'importe quelle touche.")

print("Jeu terminé, vous disposez maintenant de", argent_disponible, "euros.")
