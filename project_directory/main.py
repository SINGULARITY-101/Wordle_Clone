import os
from dotenv import load_dotenv
from openai import OpenAI

# Getting the API Key set in the environment variable 
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Constructing a new client instance
client = OpenAI(api_key = API_KEY)


# Sending the prompt request to chat GPT
def get_the_words():
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



# Function for starting the game
def start_the_game(actual_word_character_list, actual_word):
    print("Hello Player 1, you have 6 chances to guess a 5 letter word")
    attempts = 1
    print("_ _ _ _ _ \n")
    
    while(attempts<=6):
        # Checking for a valid input
        while (True):
            print(f"Enter your guess {attempts}")
            guessed_word = input()
            guessed_word_character_list = [*guessed_word]
            
            if(len(guessed_word_character_list)!=5):
                print("Invalid input! Please enter a 5 letter word\n")
                continue
            else:
                break
        
        print(guessed_word_character_list)
        
        
        # On a completely correct guess
        if guessed_word_character_list == actual_word_character_list:
            print("Congratulations, you guessed the word right!")
            break
        
        # On an incorrect guess
        for index, item in enumerate(guessed_word_character_list):
            
            if item not in actual_word_character_list:
                print(f"{item} is not in the word")
                continue
            
            if (item in actual_word_character_list) and (actual_word_character_list[index] == item):
                print(f"{item} is at the correct spot!!")
                continue
            
            if (item in actual_word_character_list) and (actual_word_character_list[index] != item):
                print(f"{item} is in the word but not at the correct sport") 
                continue
            
            
        attempts = attempts + 1 
    
    
    if(attempts == 7):
        print(f"You were not able to guess the word correctly. It was : {actual_word}")
        
    
        
        
            
        
        
    
    



    

if __name__ == "__main__":
    actual_word = get_the_words()
    actual_word = actual_word.lower().strip().rstrip(".")
    
    actual_word_character_list = [*actual_word]
    print(actual_word)
    print(actual_word_character_list)
    
    start_the_game(actual_word_character_list, actual_word)
    
    
    
    


