from colorama import Fore

# color1 = Fore.GREEN
# color2 = Fore.YELLOW
# color3 = Fore.WHITE

# print(color1 + "Here is some text in green" + Fore.RESET)
# print(color2 + "Here is some text in yellow" + Fore.RESET)
# print(color3 + "Here is some text in white" + Fore.RESET)

result_to_print = ['c at correct position', 'r at correct position', 'i at correct position', 'l not in the word', 's not in the word']
guess_list = []




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
        

display_results()

for item in guess_list:
    print(item)