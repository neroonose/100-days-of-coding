

with open("Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter:
    content = letter.read()

with open("Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Names\\invited_names.txt", mode="r") as names:
   
    for line in names:
        single_name = line.strip()
        final_letter = (content.replace("[name]", f"{single_name}"))
        with open(f"Mail+Merge+Project+Start\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_to_{single_name}.txt", mode="w") as new:
            new.write(final_letter)

#I know that 2 months from now, I wouldn't remember what I did here.