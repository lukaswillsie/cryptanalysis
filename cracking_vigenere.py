from chi_squared import letters
from utility import sort, caesar_shift, vigenere_cipher, letter_to_shift
from chi_squared import decipher

MAX_KEYWORD_LENGTH = 20;

# Using the given ciphertext, iterates through all possible keyword lengths
# between 1 and MAX_KEYWORD_LENGTH, in order of increasing index of coincidence.
# This means we visit the most likely possible keyword lengths first.
# For each possible keyword length, we use the Chi-Squared method to determine
# the most likely decryption of the resultant subsequences, and hence the most
# likely keyword. We then print the decrypted plaintext and keyword resulting
# from this analysis, before moving on the next possible keyword length
def decipher_2(ciphertext):
    ic_sorted = get_optimal_IC(MAX_KEYWORD_LENGTH, ciphertext)
    # Iterate through the list of possible keyword lengths
    for shift in ic_sorted:
        print("*************" + str(shift) + "*************")
        solution = ""
        keyword = ""
        deciphered_subsequences = []
        # Iterate through the subsequences resulting from the given
        # keyword length
        for subsequence in shift[2]:
            # Crack the given subsequence as a Caesar cipher
            results = decipher(subsequence)
            deciphered_subsequences.append(results[0][0])

            # Construct the keyword from the shift applied to the ciphertext
            letter = results[0][2]
            keyword += letters[(26 - letter_to_shift(letter)) % 26]
            
        ciphertext_index = 0
        subsequence_index = 0
        deciphered_subsequences_index = 0
        complete = False
        
        # Now that each subsequence has been cracked as a Caesar Shift,
        # reconstruct the original plaintext
        while not complete:
            if ciphertext[ciphertext_index].isalpha():
                solution += deciphered_subsequences[deciphered_subsequences_index][subsequence_index]

                deciphered_subsequences_index += 1
                if deciphered_subsequences_index >= len(deciphered_subsequences):
                    deciphered_subsequences_index = 0
                    subsequence_index += 1
            else:
                solution += ciphertext[ciphertext_index]
                
            ciphertext_index += 1
            if ciphertext_index >= len(ciphertext):
                complete = True

        print(solution)
        print("Keyword:" + keyword)
        if input("Is this the correct decryption? (y or n): ").lower() == "y":
            break
        print()
        
                    

# Takes in a ciphertext and an integer
# For each number i between 1 and num, inclusive, finds the average index 
# of coincidence of the resultant subsequences, assuming a keyword of length i
# The method then returns a list of tuples
# (i,|Average IC - 0.0667|, [subsequences])
# sorted in increasing order of the second element
# That is, the keyword lengths resulting in subsequences with average
# IC closest to 0.0667, that of normal English text, appear first in the list
def get_optimal_IC(num, ciphertext):
    subsequences = []
    array = []
    for i in range(1, num+1):
        for j in range(i):
            array.append("")

        counter = 0
        # Get subsequences of the ciphertext corresponding to key of length i
        for character in ciphertext:
            if character.isalpha():
                array[counter] = array[counter] + character
                counter += 1
                if counter >= i:
                    counter = 0

        # Calculate the average index of coincidence of the subsequences
        total = 0
        number = 0

        for subsequence in array:
            total += index_of_coincidence(subsequence)
            number += 1
            
        average = total / number
        subsequences.append( (i, abs(average - 0.0667), array) )

        
        array = []

    return sort(subsequences, True)
    
# Takes in a string and returns the Index of Coincidence of the text,
# which will be used to determine how English-like the text is
def index_of_coincidence(text):
    occurrences = {}
    for letter in letters:
        occurrences[letter] = 0


    for letter in text:
        if letter.isalpha():
            occurrences[letter.lower()] += 1

    numerator = 0
    total_count = 0

    for letter in occurrences.keys():
        numerator += occurrences[letter] * ( occurrences[letter] - 1)
        
        total_count += occurrences[letter]

    return numerator / (total_count * (total_count  - 1) )
    
if __name__ == "__main__":
    input_file = open("input.txt")
    if(file.read() == ""):
        print("Please place your input ciphertext in the \"input.txt\" file")
    else:
        decipher_2(input_file.read())
