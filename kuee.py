import os
os.system('cls')
from termcolor import colored, cprint

for i in range (1):
	cprint("&  &  &  &", "red")
	cprint("°"*10, "blue", "on_yellow")
	cprint(" "*10, "white", "on_light_blue")
	cprint("=%"*5, "blue", "on_yellow")
