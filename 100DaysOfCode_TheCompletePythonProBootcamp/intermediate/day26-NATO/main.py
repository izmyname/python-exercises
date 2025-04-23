import pandas

nato_csv = pandas.read_csv("./nato_phonetic_alphabet.csv")
# nato_letters = {}

# for (index, row) in nato_csv.iterrows():
#     nato_letters[row.letter] = row.code
nato_letters = {row.letter:row.code for (index, row) in nato_csv.iterrows()}
name = input(" Enter your name: ").upper()
nato_name = [nato_letters[l] for l in name]
print(nato_name)
