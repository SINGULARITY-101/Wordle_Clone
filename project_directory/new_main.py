import os
from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore


result_to_print = ["", "", "", "", ""]
guess_list = []



# Getting the API Key set in the environment variable 
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Constructing a new client instance
client = OpenAI(api_key = API_KEY)


# Sending the prompt request to chat GPT
def get_the_word():
    chat_completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        
        messages = [
            {
                "role":"user",
                "content":"Generate a 5 letter word for me that is in the dictionary. Do not include any explanation or punctuations."
            }
        ]
    )
    return(chat_completion.choices[0].message.content)





# Function to start the game
def start_the_game(secret_word, secret_word_list):
    print("Hello, you have 6 chances to guess a 5 letter word")
    attempts = 1
    
    
    while (attempts<=6):
        while(True):
            print("Enter your guess")
            guess = input().upper()

            if (len(guess)) != 5:
                print("Invalid Input! Please enter a 5 letter word\n")
                continue
            else:
                break
        
        output = wordle_logic(guess, secret_word, secret_word_list)
        if output == 1:
            print("Congratulations! You guessed the word correctly")
            break
        else:
            attempts = attempts + 1
            continue
    
    if attempts > 6:
        print(f"Sorry! You failed to guess the word correctly. The actual word was : {secret_word}")
    






def wordle_logic(guess, secret_word, secret_word_list):
    #On a completely correct guess
    if guess == secret_word:
        return 1
    
    else:        
        guessed_word_list = [*guess]
        secret_word_list_copy = [*secret_word_list]
        
        #Finding the correctly placed letters 
        for i in range(len(guessed_word_list)):
            letter = guessed_word_list[i]
            if letter == secret_word_list_copy[i]:
                secret_word_list_copy[i] = "*"
                result_to_print[i] = letter + " at correct position"
            else:
                continue
        
 
        #Doing a pass for the letters that are in the word but not at the correct position
        for i in range(len(guessed_word_list)):
            letter = guessed_word_list[i]
            if letter in secret_word_list_copy and secret_word_list_copy[i] != "*":
                result_to_print[i] = letter + " in the word but not at the correct position"
            
            elif secret_word_list_copy[i] == "*":
                continue
            
            else:
                result_to_print[i] = letter + " not in the word"
        


        display_results()
        for item in guess_list:
            print(item)
        
        print("\n")    
        return 0





#Function to display results after every guess 
def display_results():
    result_with_color = []
    
    for item in result_to_print:
        letter = item[0]
        if " at correct position" in item:
            color = Fore.GREEN
        
        elif " in the word but not at the correct position" in item:
            color = Fore.YELLOW
            
        else:
            color = Fore.WHITE
        
        colored_letter = color + letter + Fore.RESET
        result_with_color.append(colored_letter)
    
    guess_list.append(" ".join(result_with_color))
        
            






if __name__ == "__main__":
    secret_word = get_the_word().upper().strip().rstrip(".")
    print(secret_word)
    secret_word_list = [*secret_word]
    
    start_the_game(secret_word, secret_word_list)