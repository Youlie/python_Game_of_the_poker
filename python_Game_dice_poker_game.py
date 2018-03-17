#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from itertools import groupby

neuf = 1
dix = 2
valet = 3
reine = 4
roi = 5
aS = 6

names = { neuf:"9", dix:"10", valet:"J", reine:"Q", roi: "K", aS:"A"}

player_score = 0
computer_score = 0

def start():
    print "Jouons au jeu du Poker aux dés."
    while game():
        pass
    scores()

def game():
    print "L'ordinateur va vous aider à lancer vos 5 dés."
    throws()
    return play_again()

def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print "Dice", i +1, ":", names[dice[i]]

    result = hand(dice)
    print "Vous avez actuellement", result

    while True:
        rerolls = input("Combien de dés voulez-vous relancer ?")
        try:
            if rerolls in (1,2,3,4,5):
                break
        except ValueError:
            pass
        print "Je n'ai pas compris. Veuillez svp saisir 1,2,3,4 ou 5."
        if rerolls == 0:
            print "Vous terminez avec", result
        else:
            roll_number = rerolls
            dice_rerolls = roll(roll_number)
            dice_changes = range(rerolls)
            print "Entrez le numéro du dé que vous voulez relancer :"
            iterations = 0
            while iterations < rerolls:
                iterations = iterations +1
                while True:
                    selection = input("")
                    try:
                        if selection in (1,2,3,4,5):
                            break
                    except ValueError: 
                        pass
                    print "Je ne vous ai pas compris. Veuillez saisir 1,2,3,4 ou 5."
                    dice_changes[iterations-1] = selection-1
                    print "Vous avez changé de dés", selection

            iterations = 0
            while iterations < rerolls:
                iterations = iterations + 1
                replacement = dice_rerolls[iterations-1]
                dice[dice_changes[iterations-1]]= replacement
            
            dice.sort()
            for i in range(len(dice)):
                print "Dés", i + 1, ":" , names[dice[i]]

            result = hand(dice)
            print "Vous terminez avec", result

def roll(roll_number):
    numbers = range(1,7)
    dice = range(roll_number)
    iterations = 0
    while iterations < roll_number:
        iterations = iterations + 1
        dice[iterations-1]= random.choice(numbers)
    return dice

def hand(dice):
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]

    if dice == straight1 or dice == straight2:
        return "Suite !"
    elif dice_hand[0] == 5:
        return "Cinq cartes identiques !"
    elif dice_hand[0] == 4:
        return "Poker !"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "Full !"
        else:
            return "Brelan !"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "Deux paire."
        else:
            return "Une paire."
    else:
        return "Une carte haute."

def play_again():
    answer = raw_input("Voulez-vous rejouer? o/n :")
    if answer in ("o","O", "oui", "Oui"):
        return answer
    else:
        print "Merci d'avoir joué à notre jeu. A bientôt !"

def scores():
    global player_score, computer_score
    print "Meilleurs scores"
    print "Joueur :", player_score
    print "Ordinateur :", computer_score
start()






