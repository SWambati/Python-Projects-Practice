#the program takes user input and plugs them to a story template

name = input("Hello there. Please enter your name: \n")
option = input(f"Okay, {name}. We are going to play a simple yet fun game. Would you like to participate? (yes/no): ").lower()
if option == "yes":
    print("Okay. Let's begin.\n")
    noun1 = input("Enter a noun: ")
    plural_noun1= input("Enter a noun in its plural form: ")
    ing_verb1 = input("Enter a verb ending with -ing: ")
    plural_noun2 = input("Enter another noun in its plural form: ")
    city1 = input("Enter the name of a city: ")
    plural_noun3= input("Enter a noun in its plural form: ") 
    adjective1 = input("Enter an adjective: ")
    noun2 = input("Enter a noun: ")
    num1 = int(input("Enter a number: "))
    noun3 = input("Enter a noun: ")
    adjective2 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter a verb: ")
    plural_noun4= input("Enter a noun in its plural form: ")
    ing_verb2 = input("Enter a verb ending with -ing: ")
    num2 = int(input("Enter a number: "))
    adverb = input("Enter an adverb: ")
    noun2 = input("Enter a noun: ")
    adjective3 = input("Enter an adjective: \n")

    print(f"In 1981, the U.S. launched the first real Space {noun1}. It was named Columbia and was piloted by two brave {plural_noun1}. They had practiced {ing_verb2} for two years and were expert {plural_noun2}. Columbia took off from {city1} using its powerful first-stage {plural_noun3} and soared off into the {adjective1} blue {noun2}. At an altitude of {num1}  feet, it went into orbit around the {noun3}. For people watching from Earth, it was a/an {adjective2} sight to {verb1}! Who could really {verb2} that there were two {plural_noun4} in space? It was mind {ing_verb2}. After {num2} orbits, the shuttle landed {adverb} at an air force {noun2}. It was a/an {adjective3} day for the U.S. Space Program. ")

else:
    print("Okay. Thank you for your time")




