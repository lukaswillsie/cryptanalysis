from random import randint
from utility import sort, caesar_shift, letters, shift_to_letter, count_occurrences, get_num_letters

# Takes in a ciphertext, calculates the chi-squared number of each possible
# Caesar shift of the text, and returns a list of tuples
# (Shifted Ciphertext, Chi-Squared Number, Shift)
# in increasing order of the second element, so that the tuple with the lowest
# Chi-Squared number is first in the list
def decipher(ciphertext):
    results = []

    for i in range(0,26):
        shifted = caesar_shift(ciphertext, i)
        results.append( (shifted, chi_squared(shifted), shift_to_letter(i)) )

    return sort(results, True)

# Calculates the chi-squared number of the given string
# This is the sum over all characters in the alphabet of
# (occurrences - expected occurrences)^2 / (expected occurences)
def chi_squared(string):
    occurrences = count_occurrences(string)
    # File containing expected frequencies of letters in the English alphabet as percentages
    frequency_file = open("frequencies.txt", "r")
    chi_squared = 0
    num_letters = get_num_letters(string)
    frequencies = []
    
    for line in frequency_file:
        frequencies.append(float(line))

    for i in range(0,len(letters)):
        character = letters[i]
        chi_squared += ((occurrences[character] - (frequencies[i]*num_letters))**2)/(frequencies[i]*num_letters)

    return chi_squared

# Let's the user type in a ciphertext, then sorts the possible caesar shift decryptions
# in increasing order of chi-squared number.
# That is, the most likely decryption, followed by the second-most likely, etc.
if __name__ == "__main__":
    ciphertext = input("Type ciphertext here: ")
    results = decipher(ciphertext)
    solved = False
    counter = 0
    while not solved:
        print("Ciphertext: " + ciphertext)
        print("Shifted: " + results[counter][0])
        counter += 1
        if input("Is this the correct decryption? (y or n): ") == "y":
            solved = True
        print()
