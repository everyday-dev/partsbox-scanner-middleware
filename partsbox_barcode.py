import serial
import pyautogui
import sys

def convert_special_characters(data):
    # Replace RS, GS, EOT with {RS}, {GS}, {EOT}
    data = data.replace('\x1E', '{RS}').replace('\x1D', '{GS}').replace('\x04', '{EOT}')
    return data

def read_from_serial_port(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate)
        print(f"Connected to {ser.name}")

        while True:
            data = ser.readline().decode('utf-8').strip()
            if data:
                # Convert our string by replacing non-printable characters with their ASCII names
                converted_data = convert_special_characters(data)
                # Print out the original and converted data
                print(f"Original Data: {data}, Converted Data: {converted_data}")
                # Simulate keyboard input
                pyautogui.typewrite(converted_data)

    except serial.SerialException as e:
        print(f"Error: {e}")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed.")

# Entry point
# Read in COM port and baudrate from command line
# Example: python barcode.py /dev/ttyACM0 115200
if len(sys.argv) != 3:
    print("Usage: python partsbox_barcode.py <COM port> <baud rate>")
    sys.exit(1)

port_name = sys.argv[1]
baudrate = sys.argv[2]

# Start reading from serial port using the provided COM port
read_from_serial_port(port_name, baudrate)
