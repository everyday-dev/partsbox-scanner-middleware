# Partsbox 2D Scanner Middleware
This script acts a middleware between the 2D scanner and the Partsbox web app. It reads the barcode from the scanner via a serial port, replaces non-printable ASCII characters as needed, and send the final barcode string as a keyboard input to be picked up by Partsbox.

## Setup
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
If on linux you'll need to install the following packages:
```bash
apt install python3-tk
```

## Usage
To connec to the scanner connected to `/dev/ttyACM0` at 115200 baud:
```bash
python partsbox_barcode.py /dev/ttyACM0 115200
```