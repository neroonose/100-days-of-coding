import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato= pandas.read_csv("NATO-alphabet\\nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word:").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)