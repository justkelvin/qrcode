#!/usr/bin/env python3

import pyqrcode
import argparse
import traceback, sys
from colorama import Fore, Style
from banner import banner

def generate_qr(raw_text='', file_name=''):
    """Use pyqrcode to convert text and generate a qrcode"""        
    qr_code = pyqrcode.create(raw_text)
    print(qr_code.terminal())
    qr_code.png(f'qr_images/{file_name}.png', scale=10)

def main():
    parser = argparse.ArgumentParser(description='Creates a qrcode and a png file of the qrcode')
    parser.add_argument('-i', '--input', help='Your input text string to be converted')
    parser.add_argument('-o', '--output', help='Custom output png file.')
    args = parser.parse_args()
        
    try:
        if args.input and args.output:
            raw_text = args.input
            file_name = args.output
            print(banner())
            generate_qr(raw_text, file_name)
            
        elif args.input or args.output:
            raw_text = args.input
            file_name = args.input
            print(banner())
            generate_qr(raw_text, file_name)

        else:
            print(banner())
            raw_text = input(Fore.BLUE + '[>] Enter text to convert: ' + Style.RESET_ALL)
            file_name = raw_text
            generate_qr(raw_text, file_name)
            
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
    main()