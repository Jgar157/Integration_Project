import pygame
import math

# Jairo Garciga
# PlayerBase is the class that creates the object for the player in Zach and I's project.
# I made PlayerBase in it's entirety and Zach helped me handle some of the bugs that were brought up.
# This class consists of the player's stats, exp, hp, functions for battling, and functions for receiving items. 
# It is still a WIP.

class PlayerBase:
    # All the player variables are kept within this area.
    # Exp, health, weapons, damage, and stats will all be here.

    playerName = ""
    playerLevel = 1
    playerExp = 0
    playerExpCap = 100
    expLogistic = 0
    playerCurrentHealth = 20
    playerMaxHealth = 20
    playerWeapon = 0
    playerDamage = 0

    # The stats, Strength, Wisdom, and Agility.

    Strength = 0
    Wisdom = 0
    Agility = 0
    SkillPoints = 0

    # The constructor (place holder for now)
    def __init__(self, name):
        self.playerName = name

    # Player name Setter & Getter

    def setPlayerName(self, inputName):
        self.playerName = inputName

    def getPlayerName(self):
        return self.playerName


    # Player Level getter.

    def getPlayerLevel(self):
        return self.playerLevel

    def playerLevelUp(self):
        while self.getPlayerExp() >= self.getPlayerExpCap():
            self.playerLevel += 1
            self.incrementSkillPoints()
            self.setPlayerExp(self.getplayerExp()-self.getplayerExpCap())
            self.setPlayerExpCap()

    # Player Exp Setter and Getter.

    def addPlayerExp(self, expGained):
        self.playerExp += expGained
        self.playerLevelUp()

    def setPlayerExp(self, amount):
        self.playerExp = amount

    def getPlayerExp(self):
        return self.playerExp

    # Player ExpCap Setter, Getter, & Algorithm.

    # Multiplies the current exp cap by the multiplier from the exp algorithm to produce the new exp cap.
    def setPlayerExpCap(self):
        self.playerExpCap = int(self.playerExpCap*self.expAlgorithm())

    def getPlayerExpCap(self):
        return self.playerExpCap

    def expAlgorithm(self):
        self.ExpLogistic = 1+(1 / (3 + math.exp(-(3 / 4) * (self.playerLevel / 16) - 4)))
        Multiplier = 1 + self.ExpLogistic
        return self.ExpLogistic

    # Player health Setter, Getter, and Health calculation.

    def setPlayerCurrentHealth(self, incoming):
        self.playerCurrentHealth = incoming

    def getPlayerCurrentHealth(self):
        return self.playerCurrentHealth

    def playerHeal(self, amount):
        if amount+self.getPlayerCurrentHealth() <= self.getPlayerMaxHealth():
            self.setPlayerCurrenthealth(self.getPlayerCurrentHealth()+amount)
        else:
            self.setPlayerCurrentHealth(self.getPlayerMaxHealth())

    def playerTakeDamage(self, damage):
        self.playerCurrentHealth = self.getPlayerVurrentHealth() - damage

    def setPlayerMaxHealth(self):
        self.playermaxHealth = self.getPlayerMaxHealth()
        self.playerStrength = self.getPlayerStrength()
        self.healthCalculation = self.playerMaxHealth + self.playerStrength

    def getPlayerMaxHealth(self):
        return self.playerMaxHealth


    # Player damage Setter and Getter.

    def setPlayerDamage(self, damage):
        self.playerDamage = damage

    def getPlayerDamage(self):
        return self.playerDamage

    def playerAttack(self):
        pass

    # Attributes: Strength, Wisdom, Agility

    # Skill point Stuff.
    def incrementSkillPoints(self):
        self.SkillPoints += 1
        print("You have accrued one more skill point.")

    def setSkillPoints(self, allocation):
        self.SkillPoints += allocation

    def allocateSkillPoints(self, allocation):
        self.SkillPoints -= allocation

    def getSkillPoints(self):
        return self.SkillPoints

    # Player Strength Setter and Getter.

    def setPlayerStrength(self, allocation):
        if self.SkillPoints >= allocation:
            self.Strength += allocation
            self.allocateSkillPoints(allocation)
            playerStrength = self.getPlayerStrength()
            print("Your strength is now {}".format(playerStrength))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerStrength(self):
        return self.Strength

    # Player Wisdom Setter and Getter

    def setPlayerWisdom(self, allocation):
        if self.SkillPoints >= allocation:
            self.Wisdom += allocation
            self.allocateSkillPoints(allocation)
            playerwisdom = self.getPlayerWisdom()
            print("Your wisdom is now {}".format(playerwisdom))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerWisdom(self):
        return self.Wisdom

    # Player Agility Setter and Getter

    def setPlayerAgility(self, allocation):
        if self.SkillPoints >= allocation:
            self.Agility += allocation
            self.allocateSkillPoints(allocation)
            playeragility = self.getPlayerAgility()
            print("Your agility is now {}".format(playeragility))
        else:
            print("You only have {} to allocate, not {}.".format(self.Skillpoints, allocation))

    def getPlayerAgility(self):
        return self.Agility

    # Item affects and what to do with them
    def itemAffects(self, item):
        if item.getAffect() == 1:
            self.setPlayerCurrentHealth(item.gethealAmount())
