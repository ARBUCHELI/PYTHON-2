"""
Description: Mad Libs Game
Author: Andres R. Bucheli
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("Welcome to Mad Libs. The game has started!!!")

name = input("Enter a name: ")

adjective1 = input("Enter the first adjective: ")
adjective2 = input("Enter the second adjective: ")
adjective3 = input("Enter the third adjective: ")

verb = input("Enter a verb: ")

noun1 = input("Enter the first noun: ")
noun2 = input("Enter the second noun: ")

animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

print (STORY % (name, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3, name, superhero, name, country, name, dessert, name, year, noun2))