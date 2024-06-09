PLACEHOLDER_NAME = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as mail_file:
    mail = mail_file.read()
    for name in names:
        stripped_name = name.strip()
        new_mail = mail.replace(PLACEHOLDER_NAME, stripped_name)
        with open(f"./Output/ReadyToSend/mail_for_{stripped_name}.txt", "w") as completed_mail_file:
            completed_mail_file.write(new_mail)