#!/usr/bin/env python3

# Imports

import pyqrcode
import traceback, sys
from colorama import Fore, Style
from banner import banner

exit_text = '\n\n[!] Closing... Goodbye. (^-^)\n'
def main():
    try:
        def generate_qr():
            """Use pyqrcode to convert text and generate a qrcode"""
            raw_text = input(Fore.BLUE + '\n[>] Enter text to convert: ' + Style.RESET_ALL)
            qr_code = pyqrcode.create(raw_text)
            print(qr_code.terminal())
            qr_code.png('qr_images/qr.png', scale=10)
            
        print(banner())
        generate_qr()
            
    except KeyboardInterrupt:
        print(Fore.RED + exit_text)
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
    
if __name__ == '__main__':
    main()