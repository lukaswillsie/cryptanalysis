from random import randint

global letters
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Returns a sorted array of tuples in increasing or decreasing order
# of the SECOND ENTRY, increasing or decreasing given by the second argument
# Will work on any array of tuples provided they have size at least 2
def sort(tuples, increasing):
    if len(tuples) > 1:
        i = randint(0, len(tuples)-1)
        fulcrum = tuples[i]

        to_partition = tuples[0:i] + tuples[i+1:]

        smaller,bigger = partition(to_partition, fulcrum)
        if increasing:
            return sort(smaller, increasing) + [fulcrum] + sort(bigger, increasing)
        else:
            return sort(bigger, increasing) + [fulcrum] + sort(smaller, increasing)
    else:
        return tuples

# Partition the given array of tuples into smaller, bigger arrays
# According to SECOND ENTRY using the given fulcrum
def partition(tuples, fulcrum):
    smaller = []
    bigger = []
    for pair in tuples:
        if pair[1] <= fulcrum[1]:
            smaller.append(pair)
        else:
            bigger.append(pair)
    return (smaller,bigger)

# Encrypts and returns the given plaintext using a Caesar Cipher with the given shift
def caesar_shift(plaintext, shift):
    shifted = ""
    for character in plaintext:
        if character.isalpha():
            if character.islower():
                shifted += letters[(letters.index(character.lower())+shift) % 26]
            else:
                shifted += letters[(letters.index(character.lower())+shift) % 26].upper()        
        else:
            shifted += character

    return shifted

# Enciphers the given plaintext using the given keyword
# according to the vigenere cipher
def vigenere_cipher(plaintext, keyword):
    ciphertext = ""
    index = 0

    for character in plaintext:
        if character.isalpha():
            ciphertext += caesar_shift(character, letter_to_shift(keyword[index]))
            index += 1

            if index >= len(keyword):
                index = 0

        else:
            ciphertext += character
    return ciphertext

# Counts the total number of letters in the given text
def get_num_letters(text):
    count = 0
    for character in text:
        if character.isalpha():
            count += 1

    return count

# Counts the number of occurrences of each letter in the alphabet in the
# given text. Returns a dictionary with keys given by the lower-case
# letters of the alphabet
# The counting is case-insensitive
def count_occurrences(text):
    occurrences = {}
    for letter in letters:
        occurrences[letter] = 0

    for char in text:
        if char.isalpha():
            char = char.lower()
            occurrences[char] += 1

    return occurrences

# Takes in a number, a Caesar Shift number, and returns the letter
# that corresponds to that shift
def shift_to_letter(shift):
    return letters[shift % 26]

# Takes in a letter and returns the Caesar Shift number to which
# the given letter corresponds
def letter_to_shift(letter):
    return letters.index(letter.lower())

if __name__ == "__main__":
    pass
