import random
import time
import math

def PlayerInformation():#*This method will receive the most basic player information needed to make the game properly work.
    #IFNewGame
    #StatList = ["ATTACK", "DEFENSE", "SPEED", "CRITICAL HIT CHANCE", "CRITICAL HIT DAMAGE", ]
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
    if Profession.upper() == "MAGE": #*These set of if-statements assigns different values to the player's stats depending on what class the user inputs
        for StatName in ["ATTACK", "DEFENSE", "SPEED", "CRITICAL HIT CHANCE", "CRITICAL HIT DAMAGE"]:
            if StatName == "ATTACK":
                PlayerFile.write(StatName + ":" + " " + "2" + "\n")
            else:
                PlayerFile.write(StatName + ":" + " " + "1" + "\n")

    elif Profession.upper() =="ARCHER":
        for StatName in ["ATTACK", "DEFENSE", "SPEED", "CRITICAL HIT CHANCE", "CRITICAL HIT DAMAGE"]:
            if StatName == "ATTACK":
                PlayerFile.write(StatName + ":" + " " + "2" + "\n")
            else:
                PlayerFile.write(StatName + ":" + " " + "1" + "\n")
    elif Profession.upper() =="WARRIOR":
        for StatName in ["ATTACK", "DEFENSE", "SPEED", "CRITICAL HIT CHANCE", "CRITICAL HIT DAMAGE"]:
            if StatName == "ATTACK":
                PlayerFile.write(StatName + ":" + " " + "2" + "\n")
            else:
                PlayerFile.write(StatName + ":" + " " + "1" + "\n")  
    #IFLoadGame


def SaveEquipment():
    pass
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

