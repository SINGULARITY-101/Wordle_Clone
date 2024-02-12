import os
from dotenv import load_dotenv
from openai import OpenAI

result_to_print = ["", "", "", "", ""]
correctly_guessed_letters = ["_ ", "_ ", "_ ", "_ ", "_ "]


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
            guess = input()

            if (len(guess)) != 5:
                print("Invalid Input! Please enter a 5 letter word\n")
                continue
            else:
                break
        
        output = wordle_logic(guess, secret_word, secret_word_list)
        attempts = attempts + 1
    



# Function to grey out correctly placed letters in the secret word list 
def correct_letters(guessed_word_list, secret_word_list):
    for i in range(len(guessed_word_list)):
        letter = guessed_word_list[i]
        if letter == secret_word_list[i]:
            secret_word_list[i] = "*"
    
    return secret_word_list





def wordle_logic(guess, secret_word, secret_word_list):
    #On a completely correct guess
    if guess == secret_word:
        return 1
    
    else:
        guessed_word_list = [*guess]
        secret_word_list = correct_letters(guessed_word_list, secret_word_list)
        print(secret_word_list)






if __name__ == "__main__":
    secret_word = get_the_word().lower().strip().rstrip(".")
    print(secret_word)
    secret_word_list = [*secret_word]
    
    start_the_game(secret_word, secret_word_list)