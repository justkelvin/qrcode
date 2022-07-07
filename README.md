# **QR Code Generator**

<!-- ![prompt](qr_images/output.png) -->

## **A free and opensource tool to generate QR Codes**

This script will help you create a QR Code of the text of your choice and print it in your terminal. It will also create a high quality image in a directory to help you store the image for later use. The script now supports qr image decoding.

## **Compactibility**

Requires python3 and several pip modules which can be install easily.
The script has been tested in both **Windows** and **Linux** environments.

## **Installation**

Requires latest version of Python3 installed and several pip modules.

### **For Debian-based GNU/Linux distributions**

```linux
sudo apt install git python3 zbar
git clone https://github.com/justkelvin/qrcode.git
cd qrcode
pip3 install -r requirements.txt
./qrgenerator.py
```

### **Windows OS**

Ensure you have git and python3 installed and can run ```git --version``` and ```python3 -V``` in a commandline prompt

```windows
git clone https://github.com/justkelvin/qrcode.git
cd qrcode
pip3 install -r requirements.txt
python3 qrgenerator.py
```

## **Usage**

The script can be run  with the following options.

```bash
#Running the script without any arguments will show this nice banner
#and a prompt to enter the text you want to convert to QR Code
#The text you enter will be the file name of the output imaage file

./qrgenerator

```

![prompt](qr_images/prompt.png)

```bash
#This allows you to give the arguments without interactive prompt

./qrgenerator -i <input string> -o <output image file name>

# To decode a qr image file

./qrgenerator -d <image location>

```

![prompt](qr_images/output.png)

## **Contact me**

For Queries: [Twitter](https://twitter.com/@alias_notfound)
