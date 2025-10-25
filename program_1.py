# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names,
# and displays their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    # Split the name into separate words
    name_parts = personsName.strip().split()

    # Loop through each name part and take the first letter
    for part in name_parts:
        if part:  # make sure it's not empty
            personsInitials += part[0].upper() + ". "

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials)