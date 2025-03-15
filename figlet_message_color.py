# pip install termcolor pyfiglet
# figlet fonts http://www.figlet.org/examples.html

import pyfiglet
from termcolor import colored

def display_figlet_message(input):
	message = pyfiglet.figlet_format(input, font='doh')
        # adjust size 
        # pyfiglet.figlet_format(input, font='doh', width='<your_size>')
	colored_message = colored(message, color='green')
	print(colored_message)

display_figlet_message("Thomas")
display_figlet_message("Tam An")
