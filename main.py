import pandas


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter : row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a Word: ").upper()
letter_list = [letter for letter in word]
# nato_word_list = [value for (key, value) in nato_dict.items() if key in word]
nato_word_list = [nato_dict[letter] for letter in letter_list]
print(nato_word_list)


