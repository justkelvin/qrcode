#!/usr/bin/env python3

from os import error
import argparse
import traceback, sys, os
from banner import banner
from datetime import datetime
try:
    import pyqrcode
    from colorama import Fore, Style
except ModuleNotFoundError:
    print(banner())
    print("Install missing modules, check README.md for instructions\n")
    exit(1)

def generate_qr(raw_text='', file_name=''):
    """Use pyqrcode to convert text and generate a qrcode"""
    qr_code = pyqrcode.create(raw_text)
    print(qr_code.terminal())
    qr_code.png(f'qr_images/{file_name}.png', scale=10)
    print(Fore.GREEN + "\nYour image has been saved at " + Fore.CYAN + f"qr_images/{file_name}.png")

def main():
    parser = argparse.ArgumentParser(description='Creates a qrcode and a png file of the qrcode')
    parser.add_argument('-i', '--input', help='Your input text string to be converted')
    parser.add_argument('-o', '--output', help='Custom output png file.')
    args = parser.parse_args()

    try:
        if args.input:
            raw_text = args.input
            file_name = datetime.now().isoformat()
            print(banner())
            generate_qr(raw_text, file_name)
        
        elif args.output:
            err_msg = "Input string is required!"
            print(Fore.RED + err_msg + Fore.RESET + banner())
            os.system("./qrgenerator.py -h")
            sys.exit(1)
        
        elif args.input and args.output:
            raw_text = args.input
            file_name = args.output
            print(banner())
            generate_qr(raw_text, file_name)

        else:
            print(banner())
            raw_text = input(Fore.BLUE + '[>] Enter text to convert: ' + Style.RESET_ALL)
            file_name = datetime.now().isoformat()
            generate_qr(raw_text, file_name)

    except KeyboardInterrupt:
        exit_text = '\n\n[!] Closing... Goodbye. (^-^)\n'
        print(Fore.RED + exit_text)
        
    except ModuleNotFoundError:
        exit_text = '\n\n[!] Install missing modules and try again.\n'
        print(Fore.RED + exit_text)

    except Exception:
        traceback.print_exc(file=sys.stdout)

    sys.exit(0)

if __name__ == '__main__':
    main()