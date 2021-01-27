import colorama
import pyqrcode
import os
from colorama import Fore, Style
from tqdm import tqdm
from time import sleep
os.system("clear")



def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


def generate_qr():
	y = os.system("	figlet -w 1000 QR Code | lolcat")
	prGreen("			v2021.1")
	prCyan("	Script by 3rr0r 404")
	prPurple("	GitHub: https://github.com/n07f0und/qrcode.git")
	print("	")
	prLightGray("	------------------ Qr Code ------------------")
	print(" ")
	
################################File reading capability##############################
	path = input("Enter your file path: ")
	#path = "C:/Users/HP/Downloads/text.txt"

	fileObject = open(path, "r")
	data = fileObject.read()
	print(data)
#######################################################################################

	value = input(Fore.RED + "Enter text: " + Style.RESET_ALL)
	text = value
	url = pyqrcode.create(text)
	url.png('url.png', scale=10)
	
	for i in tqdm(range(0, 3), initial = 0,
              	desc ="Generating..."):
	    sleep(.1)

	print(url.terminal())
if __name__ == '__main__':
	generate_qr()

#Created url.png image management

print(" ")
u = input("Do you want to save QR created image file?(Y/N): ")

##########User choices##########

y = "y"
n = "n"
Y = "Y"
N = "N"

######if elif else statement todetermine whether to keep or delete url.png####

if u == y:
	prGreen("Your image is saved in your current directory")
	print(" ")
	prRed("Quiting...")
	print(" ")
	print("Bye.")
elif u == n:
	os.system("rm url.png")
	prRed("Image deleted!!")
	print(" ")
	prYellow("Quiting...")
	print(" ")
	print("Bye.")
elif u == Y:
	prGreen("Your image is saved in your current directory")
	print(" ")
	prRed("Quiting...")
	print(" ")
	print("Bye.")
elif u == N:
	os.system("rm url.png")
	prRed("Image deleted!!")
	print(" ")
	prRed("Quiting...")
	print(" ")
	print("Bye.")
else:
	prRed("You entered incorrect option!!")
	print(" ")
	prRed("Falling to default. Image successfully saved...")
	print(" ")
	prRed("Quiting...")
	print(" ")
	print("Bye.")
