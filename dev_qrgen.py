#!/usr/bin/env python3

# Imports

import pyqrcode
import argparse
import traceback, sys
from colorama import Fore, Style
from banner import banner

#If the script is run with arguments,,, Not the best though
parser = argparse.ArgumentParser(description='Creates a qrcode and a png file of the qrcode')
parser.add_argument('-i', '--input', help='Your input text string to be converted')
parser.add_argument('-o', '--output', help='Custom output png file.')
args = parser.parse_args()

def main(raw_text='', file_name=''):
    try:
        def generate_qr():
            """Use pyqrcode to convert text and generate a qrcode"""
            #raw_text = input(Fore.BLUE + '[>] Enter text to convert: ' + Style.RESET_ALL)
            qr_code = pyqrcode.create(raw_text)
            print(qr_code.terminal())
            qr_code.png(f'qr_images/{file_name}.png', scale=10)
            
        print(banner())
        generate_qr()
            
    except KeyboardInterrupt:
        exit_text = '\n\n[!] Closing... Goodbye. (^-^)\n'
        print(Fore.RED + exit_text)
    except Exception:
        traceback.print_exc(file=sys.stdout)
    except ModuleNotFoundError:
        print(Fore.RED + '[!] You have missing dependancies...')
        print(Fore.RED + '[-] Try ' + Fore.GREEN + 'pip3 install -r requirements.txt')
    sys.exit(0)
    
if __name__ == '__main__':
    if args.input and args.output:
        raw_text = args.input
        file_name = args.output
        main(raw_text, file_name)
        
    elif args.input or not args.output:
        raw_text = args.input
        file_name = args.input
        main(raw_text, file_name)
    else:
        raw_text = input(Fore.BLUE + '[>] Enter text to convert: ' + Style.RESET_ALL)
        main()