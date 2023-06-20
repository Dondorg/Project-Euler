digits = ["0", "1", "2" , "3", "4", "5", "6", "7", "8", "9"]

def generateLexiMutations(characters):
    permutations = []
    permuteCharacters("", characters, permutations)
    if len(permutations) > 999999:
        print(permutations[999999])

def permuteCharacters(builtString, characters, permutations):
    if len(characters) == 0:
        permutations.append(builtString)
        return None

    for i in range(len(characters)):
        char = characters[i]
        chars_copy = characters.copy()
        del chars_copy[i]
        permuteCharacters(builtString + char, chars_copy, permutations)

generateLexiMutations(digits)