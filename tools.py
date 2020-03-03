from utility import count_occurrences, letters, get_num_letters, sort
from chi_squared import chi_squared
from cracking_vigenere import index_of_coincidence
import numpy as np
from matplotlib import pyplot as plt

def frequency_analysis(text):
    print_report(text)
     
    plot_sorted_count(text)
    plot_expected_count(text)
    plot_unsorted_count(text)

    plt.show()

def print_report(text):
    print("**********Cryptanalysis Report**********")
    print("Chi-Squared Number: " + str(chi_squared(text)))
    print("Index of Coincidence: " + str(index_of_coincidence(text)) + "vs. 0.0667 (English)")

# Plot the expected frequencies of the letters of the English
# alphabet in an English text, sorted in decreasing order or frequency
def plot_expected_count(text):
    # Determine how many of each character should appear in the text
    # and get ready to plot this information

    index = np.arange(len(letters))
    frequency_file = open("frequencies.txt")
    num_letters = get_num_letters(text)
    expected_frequencies = []
    for line in frequency_file:
        expected_frequencies.append(float(line) * num_letters)

    to_sort = []
    for i in range(len(letters)):
        to_sort.append( (letters[i].upper(), expected_frequencies[i]) )

    to_sort = sort(to_sort, False)
    expected_letters = []
    expected_frequencies = []
    for pair in to_sort:
        expected_letters.append(pair[0])
        expected_frequencies.append(pair[1])
        
    # Plot expected counts of the text, sorted
    plt.figure()
    plt.bar(index, expected_frequencies)
    plt.xlabel("Letters", fontsize=5)
    plt.ylabel("Occurrences", fontsize=5)
    plt.xticks(index, expected_letters, fontsize=5)
    plt.title("Expected Frequency Analysis of English")

# Plot the actual frequencies of letters in the ciphertext, sorted in decreasing
# order of frequency
def plot_sorted_count(text):
    # Take the earlier counts of character in the text and sort them
    occurrences = count_occurrences(text)
    index = np.arange(len(letters))
    to_sort = []
    for i in range(len(letters)):
        to_sort.append( (letters[i].upper(), occurrences[letters[i]]) )

    to_sort = sort(to_sort, False)

    sorted_letters = []
    sorted_frequencies = []

    for pair in to_sort:
        sorted_letters.append(pair[0])
        sorted_frequencies.append(pair[1])
        
    # Plot sorted counts of the text
    plt.figure()
    plt.bar(index, sorted_frequencies)
    plt.xlabel("Letters", fontsize=5)
    plt.ylabel("Occurrences", fontsize=5)
    plt.xticks(index, sorted_letters, fontsize=5)
    plt.title("Frequency Analysis of Text, sorted")

# Plot the actual frequencies of letters in the ciphertext
# in alphabetical order
def plot_unsorted_count(text):
    # Count the number of letters in the text and get ready to plot them
    occurrences = count_occurrences(text)
    values = []

    caps = []
    for letter in letters:
        caps.append(letter.upper())
        values.append(occurrences[letter])
        
    index = np.arange(len(caps))
    
    # Plot unsorted counts of the text
    plt.figure()
    plt.bar(index, values)
    plt.xlabel("Letters", fontsize=5)
    plt.ylabel("Occurrences", fontsize=5)
    plt.xticks(index, caps, fontsize=5)
    plt.title("Frequency Analysis of Text")


if __name__ == "__main__":
    text = input("Please enter your ciphertext here: ")
    frequency_analysis(text)
