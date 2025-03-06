#get user to enter an adjective
def get_adjective():
    """Prompt user to enter an adjective.

    Return: user_adjective - the users chosen adjective.
    """
    prompt = True
    while prompt:
        user_adjective = input("Please enter an adjective. (e.g. 'big', 'long', 'old', etc.) ")
        #Check if the user did not enter anything.
        if len(user_adjective) < 1:
            print("No user input detected. PLease enter an adjective.")
        #Check if the user did entered anything beside alphabetic letters.
        elif user_adjective.isalpha() == False:
            print("Invalid input. Please enter an adjective.")
        else: 
            return user_adjective

#Get user to enter a noun

#get user to enter a verb

#get user to enter a place

#get user to enter an animal

#get user to enter an exclamation