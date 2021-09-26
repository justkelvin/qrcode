import os


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def banner(prGreen, prPurple, prCyan, prLightGray):
    os.system('clear')
    os.system("figlet -w 1000 QR Code | lolcat")
    prGreen("v2021.9")
    prCyan("Script by 3rr0r 404")
    prPurple("GitHub: https://github.com/n07f0und")
    prLightGray("------------------ Qr Code ------------------")

banner(prGreen, prPurple, prCyan, prLightGray)