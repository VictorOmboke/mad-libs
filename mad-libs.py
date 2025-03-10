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
            print("No user input detected. Please enter an adjective.")
        #Check if the user entered anything beside alphabetic letters.
        elif user_adjective.isalpha() == False:
            print("Invalid input. Please enter an adjective.")
        else: 
            return user_adjective

#Get user to enter a noun
def get_noun():
    """Prompt user to enter a noun.

    Return: user_noun - the users chosen noun.
    """
    prompt = True
    while prompt:
        user_noun = input("Please enter a noun. (e.g. 'cat', 'kitchen', 'table', etc.) ")
        #Check if the user did not enter anything.
        if len(user_noun) < 1:
            print("No user input detected. Please enter a noun.")
         #Check if the user did entered anything beside alphabetic letters.
        elif user_noun.isalpha() == False:
            print("Invalid input. Please enter an adjective.")
        else: 
            return user_noun

#get user to enter a verb
def get_verb():
    """Prompt user to enter a verb.

    Return: user_verb - the users chosen verb.
    """
    prompt = True
    while prompt:
        user_verb = input("Please enter a verb. (e.g. 'run', 'throw', 'sleep', etc.) ")
        #Check if the user did not enter anything.
        if len(user_verb) < 1:
            print("No user input detected. Please enter a verb.")
         #Check if the user entered anything beside alphabetic letters.
        elif user_verb.isalpha() == False:
            print("Invalid input. Please enter an adjective.")
        else: 
            return user_verb

#get user to enter a place
def get_place():
    """Prompt user to enter a place.

    Return: user_place - the users chosen place.
    """
    prompt = True
    while prompt:
        user_place = input("Please enter a place. (e.g. 'school', 'New York', 'gym' etc.) ")
        #Check if the user did not enter anything.
        if len(user_place) < 1:
            print("No user input detected. Please enter a place.")
         #Check if the user entered anything beside alphabetic letters.
        elif user_place.isalpha() == False:
            print("Invalid input. Please enter a place.")
        else: 
            return user_place

#get user to enter an animal
def get_animal():
    """Prompt user to enter an animal.

    Return: user_animal - the users chosen animal.
    """
    prompt = True
    while prompt:
        user_animal = input("Please enter a animal. (e.g. 'tiger', 'fish', 'crocodile', etc.) ")
        #Check if the user did not enter anything.
        if len(user_animal) < 1:
            print("No user input detected. Please enter an animal.")
         #Check if the user entered anything beside alphabetic letters.
        elif user_animal.isalpha() == False:
            print("Invalid input. Please enter an animal.")
        else: 
            return user_animal

#Create story
def create_mad_lib():
    """Create a mad-lib story using the users inputs.
    """
    adjective = get_adjective()
    noun = get_noun()
    verb = get_verb()
    place = get_place()
    animal = get_animal()
    print(f"""Once upon a time, there was a {adjective} man named Peter. Peter loved to eat {noun} and it was the highlight of his day. 
        One day Peter was {verb} and he realized that he was hungry and was craving {noun}. He went to {place} looking for his favorite meal but noticed it was being guarded by a {animal}.
        Peter realized he needed to fight the {animal}. A great battle ensued but peter was quickly overwhelmed by its sheer power and had lost. 
        The great battle between peter and the {animal} is a tale of legends that will be remembered for generations. RIP Peter.""")

create_mad_lib()