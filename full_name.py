# DS-Task-3

# Start infinite loop until break statement
while True: 
    # Ask for user input
    full_name = input('Please enter your full name: ')
    
    # Checks if every character in 'full_name' is a letter or a space.
    if all(char.isalpha() or char.isspace() for char in full_name):
        
        # Checks if less than two parts (presumably first and last names).
        if len(full_name.split()) < 2:
            print('Please enter your full name including first and surname.')
        
        # Checks if user has entered anything at all.
        elif len(full_name) == 0:
            print('You haven\'t entered anything. Please enter your full name.')
        
        # Checks if user has entered less than 4 characters.
        elif len(full_name) < 4:
            print('You have entered less than 4 characters. Please make sure that you have entered your name and surname.')
        
        # Checks if the user has entered more than 25 characters.
        elif len(full_name) > 25:
            print('You hav entered more than 25 characters. Please make sure that you have only entered your full name.')
        
        else:
            print('Thank you for entering your name.')
            
            # Breaks the infinite loop
            break
    
    # Print if input invalid
    else:
        print('Please enter only letters from the alphabet.')
