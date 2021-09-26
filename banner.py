#!/usr/bin/env python3

import random

banner1 = """
  ___  ___    ___         _     
 / _ \| _ \  / __|___  __| |___ 
| (_) |   / | (__/ _ \/ _` / -_)
 \__\_\_|_\  \___\___/\__,_\___|

"""

banner2 = """"""
banner3 = """"""
banner4 = """"""

def banner():
    banners = [banner1, banner2, banner3, banner4]
    return random.choice(banners)