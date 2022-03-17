PLACE="[name]"
with open("names.txt") as names_file:
    names=names_file.readlines()

with open("birthday_template.txt") as letter_file:
    letter_content=letter_file.read()
    for name in names:
        name=name.strip()
        new_letter=letter_content.replace(PLACE,name)
        with open(f"./Output/letter_for_{name}.txt","w") as letters:
            letters.write(new_letter)