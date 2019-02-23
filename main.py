import random
import time
import math
import os

def PlayerInformation():#*This method will receive the most basic player information needed to make the game properly work.
    #IFNewGame #todo remember to add MAX_HP to list
    StatList = ["MAX_HP", "ATTACK", "DEFENSE", "SPEED", "CRITICAL HIT CHANCE", "CRITICAL HIT DAMAGE", "MAGIC_RESIST", ]
    name = input("Greetings, what is your Name:")
    try:
        PlayerFile = open(name + '.txt', 'w')
    except PermissionError: #? I Was getting some sort of permission error when trying to run this program in command prompt(cmd).
        print("Please run this program as administrator")
    else:
        pass
    PlayerFile.write("NAME: " + name.upper() + '\n')
    time.sleep(.5)
    Profession = input("Which class would you like to pick? Warrior, Mage, Archer?:")
    PlayerFile.write("CLASS: " + Profession.upper() + '\n')
    time.sleep(.5)
    if Profession.upper() == "MAGE": #*These set of if-statements assigns different values to the player's stats depending on what class the user inputs.
        for StatName in StatList:
            if StatName == "MAGIC_RESIST":
                PlayerFile.write(StatName + ":" + " " + "3" + "\n")
            elif StatName =="MAX_HP":
                PlayerFile.write(StatName + ":" + " " + "100" + "\n")
            else:
                PlayerFile.write(StatName + ":" + " " + "1" + "\n")

    elif Profession.upper() =="ARCHER":
        for StatName in StatList:
            if StatName == "CRITICAL_HIT_CHANCE":
                PlayerFile.write(StatName + ":" + " " + "2" + "\n")
            elif StatName =="MAX_HP":
                PlayerFile.write(StatName + ":" + " " + "100" + "\n")
            else:
                PlayerFile.write(StatName + ":" + " " + "1" + "\n")
    elif Profession.upper() =="WARRIOR":
        for StatName in StatList:
            if StatName == "ATTACK" or StatName == "DEFENSE":
                PlayerFile.write(StatName + ":" + " " + "2" + "\n")
            elif StatName =="SPEED":
                PlayerFile.write(StatName + ":" + " " + "0" + "\n")
            elif StatName =="MAX_HP":
                PlayerFile.write(StatName + ":" + " " + "100" + "\n")
            else:
                PlayerFile.write(StatName + ":" + " " + "1" + "\n")  
    #IFLoadGame


def SaveEquipment():
    pass
    #os.path()
def SaveState():
    pass
def SaveInventory():
    pass
def ChoosePath():
    Path = ''
    GeneralAnswer = ['Inventory', 'CheckEquipment','CurrentHealth']
    if Path == "Inventory":
        print(Path)
    elif Path == "Inventory":
            print(Path)
    elif Path == "Inventory":
            print(Path)

def DoesItemExist(item):
    if item in open(PlayerInformation.PlayerFile, 'r').readline():
        print("True")
    else:
        print("False")

PlayerInformation()

