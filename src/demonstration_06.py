"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt:str) -> bool:
    # oCounter = 0
    # xCounter = 0

    txt = txt.lower()

    return txt.count("x") == txt.count("o")

    # for char in txt:
    #     if char == "x":
    #         xCounter += 1
    #     elif char == "o":
    #         oCounter += 1

    # if oCounter == 0 and xCounter == 0 or oCounter == xCounter:
    #     return True
    # else:
    #     return False

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))