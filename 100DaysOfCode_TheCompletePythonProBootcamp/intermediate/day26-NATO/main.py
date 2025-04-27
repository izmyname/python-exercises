import pandas

nato_csv = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_letters = {row.letter:row.code for (index, row) in nato_csv.iterrows()}

while True:
    try:
        name = input(" Enter your name: ").upper()
        nato_name = [nato_letters[l] for l in name]
    except KeyError:
        print("Use English letters only, please")
    else:
        break
    
print(nato_name)
