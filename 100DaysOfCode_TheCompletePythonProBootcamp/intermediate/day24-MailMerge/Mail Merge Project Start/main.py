#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

# take an example from ./Input/Letters/starting_letter.txt
# replace [name] placeholder with each name from ./Input/Names/invited_names.txt
# save the letters as ./Output/ReadyToSend/letter_for_[name].txt


name_list = []

with open("./Mail Merge Project Start/Input/Names/invited_names.txt", "r") as name:
    names_list = name.readlines()

for item in names_list:
    f_name = item.strip()
    name_list.append(f_name)
    
    
with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as template:
    temp_letter = template.read()
    
    

for name in name_list:
    ready_letter = temp_letter.replace("[name]", name)
    with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as invite:
        invite.write(ready_letter)